import datetime;
import json
import os

class Caching:
    def __init__(self, path: str):
        self.cache_dir = f"cache/{path}"
        
        if not self.__check_path_exists(self.cache_dir):
            self.__create_cache_dir(self.cache_dir)
       
    def __check_path_exists(self, path: str):
        return os.path.isfile(path)
    
    def __create_cache_dir(self, path: str):
        try:
            os.makedirs(path, exist_ok = True)
        except OSError as error:
            raise OSError(f"Directory {path} can not be created")
        
    def __get_cache_path(self):
        return f"{self.cache_dir}/data.json"
        
    def read(self):
        cacheExists = self.__check_path_exists(self.__get_cache_path())
        
        if not cacheExists:
            return None
        
        with open(self.__get_cache_path(), 'r') as openfile:
            return json.load(openfile)
        
    def write(self, data):
        timestamp = datetime.datetime.now().timestamp()
        
        with open(self.__get_cache_path(), "w") as outfile:
            json.dump({
                'timestamp': timestamp,
                'data': data
            }, outfile)