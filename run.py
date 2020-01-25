from Credentials import Credentials
from User import User
import random
import string

def create_user_account(first_name, last_name, username, password):
    new_user = User(first_name, last_name, username, password)
    return new_user


def save_user_details(user):
    user.save_user_details()


def check_existing_user(username, password):
    return User.user_exist(username, password)


def display_user_details():
    return User.display_user_details()


def create_new_credentials(account, f_name, l_name, email, username, password):
    new_credentials = Credentials(account, f_name, l_name, email, username, password)
    return new_credentials


def save_credentials(credentials):
    credentials.save_credentials()


def delete_credentials(credentials):
    credentials.del_account()


def find_credentials(username):
    return Credentials.get_account(username)


def display_credentials():
    return Credentials.display_accounts()


def check_existing_account(username):
    return Credentials.account_exist(username)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def main():
