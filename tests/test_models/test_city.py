#!/usr/bin/python3
"""
Test module for City model class
"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    """Test case class for city model"""

    def setUp(self):
        self.city = City()

    def test_city_has_base_class(self):
        """test if city inherit from BaseModel"""
        city = City()
        self.assertTrue(isinstance(city, BaseModel))
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_create_city_with_no_data(self):
        """test for when city is created"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
