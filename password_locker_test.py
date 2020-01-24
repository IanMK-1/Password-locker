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


if __name__ == '__main__':
    unittest.main()
