import unittest

from lesson_05.account import *

from lesson_05.account import clean_name, make_username, is_valid_email, is_valid_email_second, get_initials


class TestAccount(unittest.TestCase):
    def test_strip_space(self):
        self.assertEqual(clean_name(" sveta "), "Sveta")

    def test_capitalize(self):
        self.assertEqual(clean_name("sveta"), "Sveta")

    def test_username_from_first_last(self):
        self.assertEqual(make_username("Sveta", "Sveta"), "sveta_sveta")

    def test_valid_email(self):
        self.assertTrue(is_valid_email("sveta123@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("svate.cvft.rt"))
        self.assertFalse(is_valid_email("sveta@vbgyt"))

    def test_valid_email_second(self):
        self.assertTrue(is_valid_email_second("sveta123@gmail.com"))

    def test_invalid_email_second(self):
        self.assertFalse(is_valid_email_second("sveta123@wm.f"))

    def test_invalid_email_without_at_second(self):
        self.assertFalse(is_valid_email_second("sveta123.wm.frt"))

    def test_invalid_email_without_domain_second(self):
        self.assertFalse(is_valid_email_second("sveta123@"))

    def test_invalid_email_without_username_second(self):
        self.assertFalse(is_valid_email_second("@gmail.com"))

    def test_invalid_email_without_dot_second(self):
        self.assertFalse(is_valid_email_second("sveta123@gmailcom"))

class TestUserProfile(unittest.TestCase):

    def setUp(self):
        self.user = {
            "name": "Sveta",
            "email": "sveta123@gmail.com",
            "role": ["user"],
        }

    def test_profile_has_name(self):
        self.assertEqual(self.user["name"], "Sveta")

    def test_valid_email(self):
        self.assertTrue(is_valid_email_second(self.user["email"]))

    def test_add_role(self):
        self.user["role"].append("administrator")
        self.assertIn("administrator", self.user["role"])
        self.assertEqual(len(self.user["role"]), 2)

    def test_check_length_role(self):
        self.assertEqual(len(self.user["role"]), 1)

class TestGetInitials(unittest.TestCase):
    def test_get_normal_initials(self):
        self.assertEqual(get_initials("Sveta Sveta"), "S.S.")

    def test_str_empty_with_raise(self):
        with self.assertRaises(ValueError):
            get_initials("   ")




