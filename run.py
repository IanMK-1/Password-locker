#!/usr/bin/env python3.6
from Credentials import Credentials
from User import User
import random
import string


def create_user_account(first_name, last_name, username, password):
    """Create a new password locker account"""
    new_user = User(first_name, last_name, username, password)
    return new_user


def save_user_details(user):
    """Save user details"""
    user.save_user_details()


def check_existing_user(username, password):
    """Check if user exist using their username and password"""
    return User.user_exist(username, password)


def display_user_details():
    """display all user details"""
    return User.display_user_details()


def create_new_credentials(account, f_name, l_name, email, username, password):
    """create a new credential account"""
    new_credentials = Credentials(account, f_name, l_name, email, username, password)
    return new_credentials


def save_credentials(credentials):
    """save new credentials"""
    credentials.save_credentials()


def delete_credentials(credentials):
    """delete credential account"""
    credentials.del_account()


def find_credentials(username):
    """Find credential account using username"""
    return Credentials.get_account(username)


def display_credentials():
    """Display all credential accounts"""
    return Credentials.display_accounts()


def check_existing_account(username):
    """Check if account exists using username"""
    return Credentials.account_exist(username)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def main():
    print("Hello, welcome to Password Locker Application. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    print(
        "USE THE FOLLOWING COMMAND TO CREATE ACCOUNT: "
        "ca - create new password locker account, "
        "ex - exit"
    )
    print('\t')
    command = input().lower()

    if command == "ca":
        print("New Account")
        print("-" * 15)

        print("First Name ...")
        first_name = input()

        print("Last Name ...")
        last_name = input()

        print("Username ...")
        username = input()

        print("Password ...")
        password = input()

        save_user_details(create_user_account(first_name, last_name, username, password))
        print('\n')
        print(f"{first_name} {last_name}, New Account Created")
        print('\n')

    elif command == "ex":
        print("Goodbye..")
        exit()

    else:
        print("Goodbye..")
        exit()

    print("LOGIN:")
    print("Please enter your Username and password:")

    print("Username ..")
    su_username = input()

    print("Password ..")
    su_password = input()

    if check_existing_user(su_username, su_password):
        print(f"Welcome {first_name}")
        print("\n")
        print("Create new credential account")

        while True:
            print(
                "Use these commands: cc - create new credential account, "
                "dc - display credential account, "
                "fc - find credential account, "
                "rc - remove credential account, "
                "exc - exit"
            )

            cred_command = input().lower()

            if cred_command == "cc":
                print("New Credentials Account")
                print("-" * 15)

                print("Account e.g. instagram/facebook/twitter")
                account = input()

                print("First Name ..")
                c_first_name = input()

                print("Last Name ..")
                c_last_name = input()

                print("Email address ..")
                email = input()

                print("Username ..")
                c_username = input()

                print("Password")
                print("-" * 15)
                print(
                    "Would you like to enter password or generate password? "
                    "Use these commands: 1 - Enter own password, 2 - Generate password"
                )
                pwd_command = input()

                if pwd_command == "1":
                    print("Please enter password")
                    c_password = input()

                elif pwd_command == "2":
                    c_password = randomString()

                save_credentials(create_new_credentials(account, c_first_name, c_last_name, email, c_username,
                                                        c_password))
                print("\n")

            elif cred_command == "dc":

                if display_credentials():
                    print("List of your credential accounts")
                    print("Account | First Name | Last Name | Email | Username | Password")
                    print("-" * 70)
                    for credentials in Credentials.credentials_list:
                        print(f"{credentials.account} | {credentials.f_name} | {credentials.l_name} | "
                              f"{credentials.email} | {credentials.username} | {credentials.password}")
                        print("\n")

                    print("-" * 70)

                else:
                    print('\n')
                    print("You don't seem to have any accounts saved yet")
                    print('\n')

            elif cred_command == "fc":
                print("Enter username of credential account you want to search for")

                search_username = input()
                if check_existing_account(search_username):
                    search_account = find_credentials(search_username)
                    print(f"Your {search_account.username} credential account")
                    print("Account | First Name | Last Name | Email | Username | Password")
                    print("-" * 70)
                    print(f"{search_account.account} | {search_account.f_name} | {search_account.l_name} "
                          f"{search_account.email} | {search_account.username} | {search_account.password}")

                    print("-" * 70)

                else:
                    print("The account does not exist")

            elif cred_command == "rc":
                print("Enter username of credential account you want to delete")

                find_username = input()
                if check_existing_account(find_username):
                    found_account = find_credentials(find_username)
                    delete_credentials(found_account)

                else:
                    print("The account does not exist")

            elif cred_command == "exc":
                print("\n")
                print("Bye..")
                break

    else:
        print("\n")
        print("Wrong Username or password")
        print("Bye")
        exit()


if __name__ == '__main__':
    main()
