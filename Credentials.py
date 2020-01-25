class Credentials:
    """Class that instantiates the credentials class"""

    credentials_list = {}

    def __init__(self, f_name, l_name, email, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.username = username
        self.password = password

    def save_instagram_credentials(self):
        Credentials.credentials_list.update({'instagram': self})
