class User:
    """Class that instantiates instances of the user class"""

    user_list = []

    def __init__(self, first_name, last_name, username, password):
        """Instantiate the properties of the object"""

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user_details(self):
        """Method to save new users to a users list"""

        User.user_list.append(self)
