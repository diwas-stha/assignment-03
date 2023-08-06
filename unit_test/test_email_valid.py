import unittest
from email_valid import is_valid_email


class EmailValidTestClass(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_email("ram.shyam@gmail.com"))
        self.assertTrue(is_valid_email("ram_shyam@yahoo.com"))
        self.assertTrue(is_valid_email("ram.shyam@outlook.com"))

    def test_invalid(self):
        self.assertFalse(is_valid_email("ram shyam@gmail.com"))
        self.assertFalse(is_valid_email("ramshyam@yomail.com"))
        self.assertFalse(is_valid_email("notanemail"))
        self.assertFalse(is_valid_email("@outlook.com"))
        self.assertFalse(is_valid_email("ram shyam@gmail.com"))
        self.assertFalse(is_valid_email("ramshyam@.com"))


if __name__ == '__main__':
    unittest.main()
