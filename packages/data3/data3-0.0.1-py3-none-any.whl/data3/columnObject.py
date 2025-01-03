class new:
    def __init__(self, data):
        self.index = data[0]

        self.name = data[1]
        self.type = data[2]

        self.notnull = bool(data[3])
        self.canBeNull = not self.notnull
        self.null = self.notnull

        self.defaultValue = data[4]
        self.default = self.defaultValue
        self.dflt_value = self.defaultValue
        self.dflt = self.defaultValue

        self.primaryKey = bool(data[5])
        self.pk = self.primaryKey

    def __repr__(self):
        return str(self.name)