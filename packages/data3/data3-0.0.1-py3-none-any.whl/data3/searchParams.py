class new:
    def __init__(self, selection : str = '*', order : str = None, limit : str = None, offset : str = None) -> None:
        self.selection = selection
        self.order = order
        self.limit = limit
        self.offset = offset
    
    def __repr__(self) -> str:
        return "\n".join( [ y for x, y in {
            self.order : f"ORDER BY {self.order}",
            self.limit : f"LIMIT {self.limit}",
            self.offset : f"OFFSET {self.offset}",
        }.items() if x != None] )