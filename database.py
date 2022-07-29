import pickle
class DatabaseManager:
    """Database manager of timebox"""
    def __init__(self,database_name):
        self.database_name = database_name
    
    @staticmethod
    def _error_handler(func):
        def handler(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except Exception as e:
                raise e
        return handler

    @_error_handler
    def create_database(self):
        with open(f"{self.database_name}","wb") as file:
            pickle.dump([],file)

    @_error_handler
    def dump_data_to_database(self,data:list) -> None:
        with open(f"{self.database_name}","wb") as file:
            pickle.dump(data,file)

    @_error_handler
    def read_data_from_database(self) -> list:
        with open(f"{self.database_name}","rb") as file:
            data = pickle.load(file)
        return data

