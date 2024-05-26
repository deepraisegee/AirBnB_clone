#!/usr/bin/python3
"""
Test module for Review model class
"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestUser(unittest.TestCase):
    """Test case class for review model"""

    def setUp(self):
        self.review = Review()

    def test_review_has_base_class(self):
        """test if review inherit from BaseModel"""
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_create_review_with_no_data(self):
        """test for when review is created"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.text, "")
