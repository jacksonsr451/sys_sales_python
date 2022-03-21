class PasswordRegisterException(Exception):
    def __init__(self):
        self.message: str = str('Password is invalid format, required at least six characters!')
        super(PasswordRegisterException, self).__init__(self.message)
        