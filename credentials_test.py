import unittest
from Credentials import Credentials


class TestCredentials(unittest.TestCase):
    """TestCredentials is a sub-class that inherits properties from unittest"""

    def setUp(self) -> None:
        """Instantiate the properties of the object"""

        self.new_credentials = Credentials("luke", "shaw", "joe@gmail.com", "jluke", "password")

    def test_init(self):
        self.assertEqual(self.new_credentials.f_name, "luke")
        self.assertEqual(self.new_credentials.l_name, "shaw")
        self.assertEqual(self.new_credentials.email, "joe@gmail.com")
        self.assertEqual(self.new_credentials.username, "jluke")
        self.assertEqual(self.new_credentials.password, "password")

    def test_save_instagram_credentials(self):
        """Test_save_credentials is a test to show if user credentials are being saved"""

        self.new_credentials.save_instagram_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    
if __name__ == '__main__':
    unittest.main()
