from Credentials import Credentials
from User import User


def create_user_account(first_name, last_name, username, password):
    new_user = User(first_name, last_name, username, password)
    return new_user


