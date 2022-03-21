class EmailRegisterException(Exception):
    def __init__(self):
        self.message: str = str("Email is invalid format!")
        super(EmailRegisterException, self).__init__(self.message)
