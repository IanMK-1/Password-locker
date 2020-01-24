import unittest
from User import User
from Credentials import Credentials


class TestPasswordLocker(unittest.TestCase):
    def setUp(self) -> None:
        """Method that define instructions to be ran before each test method"""

        self.new_locker_account = User("Ian", "Mwangi", "ianmk", "1234567")

    def test_init(self):
        """Test to check if the objects are being instantiated correctly"""

        self.assertEqual(self.new_locker_account.first_name, "Ian")
        self.assertEqual(self.new_locker_account.last_name, "Mwangi")
        self.assertEqual(self.new_locker_account.username, "ianmk")
        self.assertEqual(self.new_locker_account.password, "1234567")

    def test_save_user_details(self):
        """Test_save_user_details tests if details of a new user are being saved"""

        self.new_locker_account.save_user_details()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self) -> None:
        """tearDown method define instruction to be run before each test method"""

        User.user_list = []

    def test_save_multiple_user_details(self):
        """Test_save_multiple_user_details saves details of multiple users"""

        self.new_locker_account.save_user_details()
        user_test_details = User("joe", "mark", "joe123", "lockedaccount")
        user_test_details.save_user_details()

        self.assertEqual(len(User.user_list), 2)


if __name__ == '__main__':
    unittest.main()
