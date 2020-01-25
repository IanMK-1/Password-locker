from Credentials import Credentials
from User import User


def create_user_account(first_name, last_name, username, password):
    new_user = User(first_name, last_name, username, password)
    return new_user


def save_user_details():
    User.save_user_details()


def check_existing_user(username, password):
    return User.user_exist(username, password)


