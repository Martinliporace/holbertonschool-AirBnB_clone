#!/usr/bin/python3
"""Unittests for models/user_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        """test with descriptive name"""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """test with descriptive name"""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """test with descriptive name"""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """test with descriptive name"""
        self.assertEqual(datetime, type(User().created_at))


if __name__ == "__main__":
    unittest.main()
