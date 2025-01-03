This module is meant to be used in small to medium scale applications and makes SQLite3 Read and Write functions python.
Changing every DataBase, Table and Row object to classes.

# Quickstart
```cmd
pip install data3
```
1. To get the entire DataBase use:
   ```py
   import data3
   
   with data.open() as db:
     pass
   ```
   Alternatively, you can use the following code to get just one table:
   ```py
   with data.open(table="YourTable") as table:
      pass
   ```
   Data3 will automatically open and close connections for you.
2. Index a table with `databaseObject["YourTable"]`
3. Read data with `table.get()`, you can narrow down your search by using `table.get(column=value)` or use `table.first()` to get only the first value
4. Adding/updating/removing data works as following: `table.add(column=value, column=value...)`, `table.update(column=value)(column=value, column=value...)`, `table.remove(column=value)`.
5. By adding, finding or updating data you will be returned a `rowObject` which you can index with columns to find one value, you can use `rowObject.pk` to get just the primaryKey, it can also be converted to a Dict or you can edit your row by using `rowObject["column"] = value` or `rowObject(column=value, column=value)`

# Example
```py
import data3

with data3.open(table = "matches") as table:
    for row in table.find(): # This will loop through every row as a rowObject.
        row["started"] = True # A row object can be changed with a set architecture for a single column.
        row(started = True) # Or you can call it for multiple.
    
    table.update(5)(started = False) # Here no key is provided, data3 will search for a primaryKey column or use the first column to find "5". As the table.update function will return another function in which you can specify every column and value you want to change.

    table(id = 90, started = False) # You can call a table to add a value or use "table.add".

    print(table.first(3)["started"]) # You can get one column like this also.

    with table.pause(): # Pause will temporarily close the connection and re-open it once you're done, useful when doing large computations that don't require reading the file.
        print("Free from the database.")

    print("Back to reading and writing.")

    table.remove(3) # Here no key is provided, data3 will search for a primaryKey column or use the first column to find "3". If you do want to specify a column you can use .remove(column = value).
```  

# Edit default values
```py
import data3

# These are the default values and you can edit them accordingly
data3.path = './'
data3.defaultFile = "data"
data3.fileExtension = ".db"
data3.defaultTimeout = 10

# This is the default onError function, which you can modify
def onError(error, cmd):
    print(f"[Error\t] {error}\n[input\t] {cmd}")
data3.onError = onError
```
