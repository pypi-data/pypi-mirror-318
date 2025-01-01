import os
import sys
from typing import Callable, Any

from dbpoint.dbpoint import Hub
from dapu.context import DapuContext
from dapu.perks import halt, real_path_from_list, replace_dict, is_interactive
from dapu.perks import reconf_logging, get_custom_logger, version_string_from_timeint
from dapu.perks import interpret_string_as_yaml, read_content_of_file

logging = get_custom_logger('dapu') # here we cannot use standard imported logging module! and must do it over the corner   


class DapuProcess:
    """
    All Dapu processes behave somehow similar way 
    """
    
    context: DapuContext | None = None # class variable, mostly for our wise decorator 

    def __init__(self, args: list | DapuContext | None):
        """
        Two correct way to initialize: using list of arguments to create Context, and using existing Context to keep it
        """

        if args is None:
            if DapuProcess.context is None:
                halt(3, "Wrong initialization") # wasn't given and we don't have it here neither
            self.context = DapuProcess.context
            return
        
        if isinstance(args, DapuContext):
            self.context = args
            DapuProcess.context = self.context
            logging.debug(f"from object, work_dir is {DapuProcess.context.work_dir}")
            return
        
        if isinstance(args, list):
            # argument is not DapuContext, so context must be generated, assumably for very first process in chain
            work_dir = real_path_from_list(args) # first argument is working directory
            if work_dir is None:
                halt(3, "No project (work) directory specified")
            self.context = DapuContext(work_dir)
            #self.context.work_dir = work_dir
            self.context.flags = args[1] if len(args) > 1 and args[1] is not None else []
            self.context.more_args = args[2:] # lets keep in instance var list having values starting from third from 
            self.context.LOG_LEVEL = 10 if 'debug' in self.context.flags else 20 # here we cannot use standard imported logging module! use numbers!
            reconf_logging(self.context.LOG_LEVEL) # after that line real use of logging can appear
            self.load_project_connections() # this function uses self.context (reads consts and fills self.context.profiles) 
            if not self.context.profiles.profile_exists(self.context.PROFILE_TYPE_SQL, self.context.TARGET_ALIAS): # check if sql + target exists
                halt(10, f"Cannot work without connection named as '{self.context.TARGET_ALIAS}'")
            self.context.hub = Hub(self.context.profiles.profiles_get(self.context.PROFILE_TYPE_SQL)) # dbpoint gets all sql-type profiles 
            if not self.check_stopper():
                halt(4, "Cannot run any more (newer version of me is present)")
            DapuProcess.context = self.context
            logging.debug(f"from list, work_dir is {DapuProcess.context.work_dir}")


    def check_stopper(self) -> bool:
        """
        Prevents execution it newer version is unleached. 
        Current version is stored in code (context.MYVERSION) and Last version is store in database (meta.stopper.allowed_version)
        If current is lower then prevent. If current is higher then update database (so old instances in wild can be prevented).
        Can be executed before tables are done, so error in select can be interpreted as missing table and lets continue.
        If table exists we can handle both cases: no rows and one row (if more then last taken, but updated will be all)
        """
        stopper = self.context.find_registry_table_full_name('stopper')
        sql = f"""SELECT allowed_version FROM {stopper} ORDER BY id DESC LIMIT 1""" # there is one row actually
        try:
            result_set = self.context.target(sql)
        except Exception as e1:
            # error may happen on very first execution then tables are not present yet
            # in this case we just ignore everything and we are sure that in next run it will work
            return True
        allowed_version = 0
        no_rows = True
        if result_set and result_set[0]:
            allowed_version = result_set[0][0]
            no_rows = False
        if self.context.MYVERSION < allowed_version: # cannot execute any more
            logging.info(f"My version is {self.context.MYVERSION}, allowed version is {allowed_version}")
            return False
        if self.context.MYVERSION > allowed_version: # update database with my number
            if no_rows:
                sql_upd = f"""INSERT INTO {stopper} (allowed_version) VALUES ({self.context.MYVERSION})"""
            else:
                sql_upd = f"""UPDATE {stopper} SET allowed_version = {self.context.MYVERSION} WHERE true""" # one record
            self.context.target(sql_upd, False)
            logging.info(f"Stopper version updated to {self.context.MYVERSION}")
        return True


    def load_project_connections(self) -> None:
        """
        Loads all three types of profiles into self.context.profiles
        """
        conf_files = [self.context.CONF_SQL_FILE_NAME, self.context.CONF_FILE_FILE_NAME, self.context.CONF_API_FILE_NAME]
        types = ['sql', 'file', 'api']
        for pos, type in enumerate(types):
            file_full_name = self.context.full_name_from_conf(conf_files[pos])
            logging.debug(f"Reading file {file_full_name} for {type}") 
            text_content = read_content_of_file(file_full_name)
            if text_content:
                list_of_profiles: list[dict] | None = interpret_string_as_yaml(text_content)
                if list_of_profiles:
                    self.context.profiles.profiles_add(type, [replace_dict(profile) for profile in list_of_profiles])
                else:
                    logging.debug(f"File {file_full_name} interpretation asYAML gives empty list")
            else:
                logging.debug(f"File {file_full_name} is empty or not existing")
                       
    
    def check_for_schema(self, schema_name: str, create_if_missing: bool=True) -> bool:
        """
        Using Postgre meta-knowledge asks if schema exists
        """
        schema_name = schema_name.replace("'", "")
        sql_sch = f"SELECT count(*) FROM information_schema.schemata WHERE schema_name = '{schema_name}'"
        result_set = self.context.target(sql_sch)
        if result_set[0][0] > 0: # schema exists
            return True
        
        if create_if_missing: # FIXME creation add-ons are needed probably
            sql_cre = f"""CREATE SCHEMA IF NOT EXISTS {schema_name}""" # we miss here: alter default priviledges, grant usage etc
            self.context.target(sql_cre, False) # let it crash if problem (it is really fatal)
            msg = f"Schema '{schema_name}' created"
            logging.info(msg)
            return True
        
        return False
    
    
    def find_task_dir_path(self, task_id: str, must_exists: bool=False) -> str:
        """
        Full path from task_id (gives 3 directories) and self.context root path (work_dir)
        """
        #logging.debug(f"TASK {task_id}")
        if not task_id:
            logging.error(f"Empty task_id {task_id}")
            return None
        if self.context.work_dir is None:
            logging.error(f"Context work_dir is missing for task {task_id}")
            return None
        path_way: list = task_id.split('.')
        if len(path_way) < 3:
            logging.error(f"Too short task_id {task_id}")
            return None
        path: str = self.context.full_name_from_pull(path_way)
        if must_exists and not os.path.exists(path):
            logging.error(f"Path {path} for task '{task_id}' not exists in local file system")
            return None
        return path
    

    def find_task_file_path(self, task_id: str, file_in_task: str, must_exists:bool=False) -> str:
        """
        Very similar to prev, but the name carries difference
        """
        #logging.debug(f"TASK {task_id}, FILE {file_in_task}")
        if not task_id:
            logging.error(f"Empty task_id {task_id}")
            return None
        if not file_in_task:
            logging.error(f"Empty file_in_task {file_in_task} fot {task_id}")
            return None
        if self.context.work_dir is None:
            logging.error(f"Context work_dir is missing for {file_in_task}")
            return None
        path_way: list = task_id.split('.')
        path_way.append(file_in_task)
        if len(path_way) < 4:
            logging.error(f"Too short task_id {task_id} OR missing file")
            return None
        path: str = self.context.full_name_from_pull(path_way)
        if must_exists and not os.path.exists(path):
            return None
        return path


    def find_route_dir_path(self, route_code: str, must_exists:bool=False) -> str:
        # joins together working directory and route code assuming that latter is subfolder
        # returns None on errors      
        if not route_code:
            logging.error(f"Empty route_code {route_code}")
            return None
        if self.context.work_dir is None:
            logging.error(f"Context work_dir is missing for route {route_code}")
            return None
        path: str = self.context.full_name_from_pull(route_code)
        if must_exists and not os.path.exists(path):
            logging.error(f"Path {path} for route '{route_code}' not exists in local file system")
            return None
        return path


    def get_database_time(self, precise_time: bool=True):
        """
        Time in target database as ISO string
        """
        if precise_time:
            sql = "SELECT clock_timestamp()" # Very current time (inside transaction)
        else:
            sql = "SELECT current_timestamp" # Transaction beginning time
        result_set = self.context.target(sql)
        if result_set:
            return result_set[0][0] # ISO string
        return None
    

    def connect_main(self):
        """
        Due connection is always automatic, for validation you must run some safe SQL Select
        """
        if self.get_database_time(False) is None:
            raise Exception("Connection validation failed")


    def disconnect_main(self):
        self.context.disconnect_target()
    
    
    def disconnect_all(self):
        self.context.disconnect_all()
        

    def version(self, do_log=True, do_print=False) -> str:
        if is_interactive():
            ver_info = 'noname x.x.x'
        else:
            # FIXME järgmine rida ei tööta kui on nt jupyter vms interpreeter
            path = sys.modules[self.__module__].__file__ # tegeliku alamklassi failinimi
            name = os.path.basename(path).split(os.path.sep)[-1]
            ver = version_string_from_timeint(os.path.getmtime(path)) # local time (good enough)
            ver_info = f"{name} {ver}"
        if do_print:
            print(ver_info)
        if do_log:
            logging.info(ver_info)
        return ver_info

    @classmethod
    def task_id_eventlog(cls, flag: str, content: str|None = None) -> Callable: # decorator! very special!
        """
        Decorator will insert worker_log record with desired flag. And return INT (number of rows got).
        Use decorator for function which returns result set (list on tuples) where 1st in tuple is task_id.
        Uses cls.context - so it must remain as class variable (somehow duplicating instance variable)
        """
        flag = flag.upper().replace("'", "").strip()
        content_literal = "NULL"
        if content is not None:
            content = content.replace("'", "").strip()
            content_literal = f"'{content}'"

        def inner(func: Callable[..., list[tuple]]) -> Callable:
            def wrapper(*args: Any, **kwargs: Any) -> int:
                result_set = func(*args, **kwargs)
                if result_set is None: # error
                    return None
                if not result_set: # empty
                    logging.debug(f"No result for {flag}")
                    return 0

                worker_log = cls.context.find_registry_table_full_name('worker_log')
                try:
                    for changed_row in result_set:
                        changed_row_task_id = changed_row[0]
                        if cls.context.worker_id is None:
                            worker_literal = "NULL"
                        else:
                            worker_literal = cls.context.worker_id
                        sql_reg_log = f"""INSERT INTO {worker_log} (worker, task_id, flag, content) 
                            VALUES ({worker_literal}, '{changed_row_task_id}', '{flag}', {content_literal})"""
                        cls.context.target(sql_reg_log, False)
                    count_of_logged = len(result_set)
                    logging.info(f"{count_of_logged} for {flag}") 
                    return count_of_logged
                except Exception as e1:
                    logging.error(f"during task log {e1}")
                    return None
            return wrapper
        return inner