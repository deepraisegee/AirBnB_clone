#!/usr/bin/python3
"""
Test module for User model class
"""
import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test case class for user model"""

    def setUp(self):
        self.user = User()

    def test_user_has_base_class(self):
        """test if user inherit from BaseModel"""
        user = User()
        self.assertTrue(isinstance(user, BaseModel))
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_create_user_with_no_data(self):
        """test for when user is created"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
