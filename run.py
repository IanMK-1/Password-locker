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

            cred_command = input()

            if cred_command == "cc":
                print("New Credentials Account")
                print("-" * 15)

                print("Account ..")
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
                    c_password = input()

                elif pwd_command == "2":
                    c_password = randomString()

                save_credentials(create_new_credentials(account, c_first_name, c_last_name, email, c_username,
                                                        c_password))
                print("\n")

            elif cred_command == "exc":
                print("Bye")
                break

    else:
        print("\n")
        print("Wrong Username or password")
        print("Bye")
        exit()


if __name__ == '__main__':
    main()
