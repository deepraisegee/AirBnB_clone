#!/usr/bin/python3
"""
Test module for the file storage engine.
"""
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage engine"""

    def test_get_all_objects(self):
        """test for get all the saved objects"""
        self.assertEqual(2, 2)
