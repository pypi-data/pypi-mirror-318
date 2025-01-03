from . import tableObject
import sqlite3

class new:
    def __init__(self, parent) -> None:
        self.cursor = parent.cursor
        self.parent = parent
        self.onError = parent.onError

        class pause:
            def __init__(x, callback = None) -> None: self.callback = callback
            def __enter__(x) -> None: return self.stop(self.callback)
            def __exit__(x, exc_type, exc_val, exc_tb) -> None:
                if exc_tb != None:
                    self.onError(exc_val, None)
                return self.resume(self.callback)
        self.pause = pause

    def getTables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [tableObject.new(x[0], self.cursor) for x in self.cursor.fetchall()]
    
    def __getitem__(self, table : str) -> tableObject.new:
        return tableObject.new(table, self)

    def execute(self, cmd : str) -> None:
        if self.parent.dbClosed:
            self.onError(f"Attempt to execute with {self.parent.path} database closed.", cmd)
            return
        try:
            self.cursor.execute(cmd)
        except Exception as e:
            self.onError(e, cmd)

    def fetchall(self):
        if self.parent.dbClosed:
            self.onError(f"Attempt to execute with {self.parent.path} database closed.", "Fetchall.")
            return []
        return self.parent.cursor.fetchall()

    def string(self, text : str) -> str:
        return f"\"{text}\""
    
    def stop(self, callback = None) -> None:
        self.parent.connect.commit()
        self.parent.connect.close()

        self.parent.dbClosed = True
        return callback or self

    def resume(self, callback = None) -> None:
        self.parent.connect = sqlite3.connect(self.parent.path, timeout=self.parent.timeout)
        self.parent.cursor = self.parent.connect.cursor()
        self.cursor = self.parent.cursor
        self.fetchall = self.parent.cursor.fetchall

        self.parent.dbClosed = False
        return callback or self
    
    