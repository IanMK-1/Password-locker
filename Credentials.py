class Credentials:
    """Class that instantiates the credentials class"""

    credentials_list = []

    def __init__(self, account, f_name, l_name, email, username, password):
        self.account = account
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.username = username
        self.password = password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    # @classmethod
    # def get_account(cls, username):
    #     for user_account in cls.credentials_list:
    #         if user_account.username == username:
    #             return user_account

