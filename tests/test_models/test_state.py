#!/usr/bin/python3
"""
Test module for State model class
"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestUser(unittest.TestCase):
    """Test case class for state model"""

    def setUp(self):
        self.state = State()

    def test_state_has_base_class(self):
        """test if state inherit from BaseModel"""
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_create_state_with_no_data(self):
        """test for when state is created"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
