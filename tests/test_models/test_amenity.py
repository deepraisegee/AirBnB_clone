#!/usr/bin/python3
"""
Test module for Amenity model class
"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """Test case class for amenity model"""

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_has_base_class(self):
        """test if amenity inherit from BaseModel"""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_create_amenity_with_no_data(self):
        """test for when amenity is created"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
