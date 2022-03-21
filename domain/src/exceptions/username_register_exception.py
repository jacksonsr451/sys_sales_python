class UsernameRegisterException(Exception):
    def __init__(self):
        self.message: str = str('Username is invalid format, required at least six characters!')
        super(UsernameRegisterException, self).__init__(self.message)
        