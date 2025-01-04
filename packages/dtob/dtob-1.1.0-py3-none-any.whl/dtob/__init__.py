class DictToObject:
    def __init__(self,data:dict):
        
        for key, value in data.items():
            if not hasattr(self,key):
                setattr(self, key, DictToObject(value) if isinstance(value, dict) else value)