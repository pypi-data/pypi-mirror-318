from . import columnObject
from . import searchParams
from . import rowObject

class new:
    def __init__(self, table : str, db) -> None:
        self.db = db
        self.table = table
        self.name = table

        self.pk = None
        self.columns = None
        self.onError = db.onError

        def getColumns(self):
            self.db.execute(f"PRAGMA table_info({self.table});")

            self.columns = [columnObject.new(x) for x in self.db.fetchall()]

            if len(self.columns) == 0:
                self.onError(f"No table \"{self.name}\" in \"{self.db.parent.path}\". Or the table has no columns.", None)

            self.pk = self.columns[0]

            for column in self.columns:
                if column.pk:
                    self.pk = column
                    break
            
            return self.columns
        
        self.getColumns = getColumns
        getColumns(self)

        self.pause = lambda : db.pause(self)
        self.stop = lambda : db.stop(self)
        self.resume = lambda : db.resume(self)
    
    def find(self, pkValue : str = None, searchParams : searchParams.new = searchParams.new(), **kwargs) -> list:
        whereClause = ""

        if len(kwargs) > 0:
            kwargs = list(kwargs.items())
            whereClause = f"WHERE {kwargs[0][0]} = {self.db.string(kwargs[0][1])}"
        elif pkValue != None:
            whereClause = f"WHERE {self.pk.name} = {self.db.string(pkValue)}"

        self.db.execute(f"SELECT * FROM {self.table} {whereClause} {searchParams}")

        return [rowObject.new(self, list(x)) for x in self.db.fetchall()]
    search = find
    get = find

    def first(self, *args, **kwargs) -> list:
        result = self.find(*args, **kwargs)
        if len(result) > 0:
            return result[0]
        return None
    findFirst = first
    getFirst = first
    searchFirst = first

    def add(self, pkValue = None, **kwargs):
        if pkValue:
            kwargs[self.pk.name] = pkValue

        args = list(kwargs.items())

        self.db.execute(f"""INSERT INTO {self.table} 
                        ({", ".join([x[0] for x in args])}) 
                        VALUES ({", ".join([self.db.string(x[1]) for x in args])})""")
        

        for x in self.columns:
            if not x.name in kwargs:
                kwargs[x.name] = None

        return rowObject.new(self, [kwargs[x] for x in kwargs])
    new = add
    set = add
    __call__ = add
    
    def update(self, **kwargs):
        whereClause = ""

        if len(kwargs) > 0:
            kwargs = list(kwargs.items())
            whereClause = f"WHERE {kwargs[0][0]} = {self.db.string(kwargs[0][1])}"
        else:
            self.onError("No where clause provided.", None)
            return self
        
        def updateRow(**kwargs):
            self.db.execute(f"""UPDATE {self.table}
                            SET {", ".join([f"{x} = {self.db.string(kwargs[x])}" for x in kwargs])}
                            {whereClause}""")
            return self
            
        return updateRow
    
    def delete(self, **kwargs):
        whereClause = ""

        if len(kwargs) > 0:
            kwargs = list(kwargs.items())
            whereClause = f"WHERE {kwargs[0][0]} = {self.db.string(kwargs[0][1])}"
        else:
            self.onError("No where clause provided.", None)
            return self
        
        self.db.execute(f"DELETE FROM {self.table} {whereClause}")

        return self
    remove = delete
    
    def __sub__(self, name: str) -> None:
        self.delete(**{self.pk.name : name})
        return self