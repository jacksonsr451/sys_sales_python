class InsertException(Exception):
    def __init__(self, table_name: str):
        self.message = "Insert error in table: {}".format(table_name)
        super(InsertException, self).__init__(self.message)
