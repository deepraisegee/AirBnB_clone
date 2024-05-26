#!/usr/bin/python3
"""
Test module for Place model class
"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
    """Test case class for place model"""

    def setUp(self):
        self.place = Place()

    def test_place_has_base_class(self):
        """test if place inherit from BaseModel"""
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_create_place_with_no_data(self):
        """test for when place is created"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(isinstance(place.number_rooms, int))
        self.assertTrue(isinstance(place.amenity_ids, list))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.latitude, 0.0)
