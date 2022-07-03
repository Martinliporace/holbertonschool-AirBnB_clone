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
from models.user import User

    class TestUser_instantiation(unittest.TestCase):
        """Unittests for testing instantiation of the User class."""

        
        def test_no_args_instantiates(self):
            """test with descriptive name"""
            self.assertEqual(User, type(User()))

