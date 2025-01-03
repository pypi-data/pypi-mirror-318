import sqlite3

from . import databaseObject

path = './'
defaultFile = "data"
fileExtension = ".db"
defaultTimeout = 10

def onError(error, cmd):
    print(f"[Error\t] {error}\n[input\t] {cmd}")

class open():
    def __init__(self, file : str = defaultFile, table : str = None, timeout : int = defaultTimeout) -> None:
        self.path = path + file.rstrip(fileExtension) + fileExtension
        self.timeout = timeout
        self.table = table
        self.onError = onError
        self.dbClosed = False

    def __enter__(self) -> databaseObject.new:
        self.connect = sqlite3.connect(self.path, timeout=self.timeout)
        self.cursor = self.connect.cursor()

        self.db = databaseObject.new(self)

        if self.table != None:
            self.db = self.db[self.table]

        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type != None:
            onError(exc_val, "While using DB object.")

        try:
            if not self.dbClosed:
                self.connect.commit()
                self.connect.close()
        except Exception as e:
            onError(
                e, "Close DB."
            )
