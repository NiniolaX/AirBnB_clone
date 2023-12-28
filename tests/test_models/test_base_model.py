#!/usr/bin/python3
"""Unit test for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class"""

    def setUp(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_initiator(self):
        """Tests the class constructor"""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(self.model2, BaseModel)

    def test_attr_id(self):
        """Tests the id attribute of instance"""
        self.assertTrue(hasattr(self.model1, 'id'))
        self.assertIsInstance(self.model1.id, str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_attr_created_at(self):
        """Tests the created_att attribute of instance"""
        self.assertTrue(hasattr(self.model1, 'created_at'))
        self.assertIsInstance(self.model1.created_at, datetime)

if __name__ == "__main__":
    unittest.main()
