#!/usr/bin/python
"""
test Class User
"""


import unittest
import models
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Test User """

    def test_docs(self):
        """ test for documentation """

        self.assertIsNotNone(User.__doc__)

    def test_class(self):
        """ test for class and subclass """

        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        """ test instance of User """

        test = User()
        self.assertEqual(test.email, "")
        self.assertEqual(test.password, "")
        self.assertEqual(test.first_name, "")
        self.assertEqual(test.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()