class DictToObject:
    def __init__(self,data:dict):
        
        for key, value in data.items():
            if not hasattr(self,key):
                setattr(self, key, self.convert_to_object(value))

    def __getattr__(self,name):
        if hasattr(self,name):
            return getattr(self, name)
        else:
            from termcolor import colored
            print(colored(f"No attribute '{name}' found in {self.__class__.__name__} but it was set to None to avoide errors",'red'))
            return None