class DictToObject:
    def __init__(self,data:dict):
        self.data = data
        for key, value in data.items():
            if not hasattr(self,key):
                setattr(self, key, DictToObject(value) if isinstance(value, dict) else value)
        
    def __len__(self):
        
        return len(self.data.values)