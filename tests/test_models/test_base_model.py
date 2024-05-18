#!/usr/bin/python3
"""
A module to test all the components of the base model.
"""
import unittest
import uuid
from datetime import datetime as dt

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Base Test Case for the base model"""

    def setUp(self):
        """a setup method to prepare the test fixture"""
        self.obj = BaseModel()

    def test_str_method_on_an_instance(self):
        """test for format printing of an instance"""
        self.assertEqual(
                str(self.obj),
                "[{}] ({}) {}".format(
                     self.obj.__class__.__name__,
                     self.obj.id,
                     self.obj.__dict__
                )
            )

    def test_instance_id_and_uuid(self):
        """test instance uuid"""
        self.assertIsInstance(self.obj.id, str)
        self.assertIn("-", self.obj.id)

    def test_instance_creation_timestamp(self):
        """test the timestamp of instance when created"""
        self.assertTrue(self.obj.created_at, dt.now())
        self.assertIsInstance(self.obj.created_at, dt)

    def test_when_instance_is_updated(self):
        """test for when the instance is updated"""
        self.obj.test_attr = "test"
        self.obj.save()
        self.assertTrue(self.obj.updated_at, dt.now())

    def test_to_dict_method_of_the_instance(self):
        """test the to_dict method for appropriate date return"""
        self.assertIn("__class__", self.obj.to_dict())


if __name__ == "__main__":
    unittest.main()
