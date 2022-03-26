class UserIDRequiredSTRException(Exception):
    def __init__(self):
        self.message: str = "User ID required type String"
        super(UserIDRequiredSTRException, self).__init__(self.message)
        