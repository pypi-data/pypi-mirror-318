class new:
    def __init__(self, table, values : list) -> None:
        self.table = table
        self.columns = table.columns
        self.values = values

        self.pk = self.__dict__()[self.table.pk.name]
        self.primary = self.pk

    def __dict__(self) -> dict:
        return {self.columns[i].name : self.values[i] for i in range(len(self.columns))}
        
    def __repr__(self) -> str:
        return str(self.__dict__())
    
    def __getitem__(self, column : str) -> str:
        for i in range(len(self.columns)):
            if self.columns[i].name == column:
                return self.values[i] or None
        return None
    
    def __setitem__(self, column : str, value : str):
        self.update(**{column : value})
    
    def update(self, **kwargs):
        self.table.update(**{self.table.pk.name : self.__dict__()[self.table.pk.name]})(**kwargs)
        return self
    
    __call__ = update
    edit = update
    change = update