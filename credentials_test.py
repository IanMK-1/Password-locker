import unittest
from Credentials import Credentials


class TestCredentials(unittest.TestCase):
    """TestCredentials is a sub-class that inherits properties from unittest"""

    def setUp(self) -> None:
        """Instantiate the properties of the object"""

        self.new_credentials = Credentials("instagram", "luke", "shaw", "joe@gmail.com", "jluke", "password")

    def test_init(self):
        """Test to check if the objects are being instantiated correctly"""

        self.assertEqual(self.new_credentials.account, "instagram")
        self.assertEqual(self.new_credentials.f_name, "luke")
        self.assertEqual(self.new_credentials.l_name, "shaw")
        self.assertEqual(self.new_credentials.email, "joe@gmail.com")
        self.assertEqual(self.new_credentials.username, "jluke")
        self.assertEqual(self.new_credentials.password, "password")

    def test_save_credentials(self):
        """Test_save_credentials is a test to show if user credentials are being saved"""

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self) -> None:
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        """test_save_multiple_credentials test checks if multiple credentials are being saved"""

        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "john", "hayes", "jh@ymail.com", "jhayes", "mountain")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_get_account_by_username(self):
        """test_get_account_by_username checks if user account gotten matches the username provided"""

        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "john", "hayes", "jh@ymail.com", "jhayes", "mountain")
        test_credentials.save_credentials()

        got_account = Credentials.get_account("jhayes")
        self.assertEqual(got_account.f_name, test_credentials.f_name)

    def test_del_account(self):
        """test_del_account test checks if account using username is deleted"""

        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "john", "hayes", "jh@ymail.com", "jhayes", "mountain")
        test_credentials.save_credentials()

        got_account = Credentials.get_account("jhayes")
        got_account.del_account()
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == '__main__':
    unittest.main()
