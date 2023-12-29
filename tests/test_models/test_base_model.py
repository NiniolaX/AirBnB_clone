#!/usr/bin/python3
"""Unit test for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta

class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class"""

    def setUp(self):
        """Set up BaseModel object for testing"""
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_constructor(self):
        """Tests the class constructor"""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(self.model2, BaseModel)

    def test_attr_id(self):
        """Tests the id attribute of instance"""
        self.assertTrue(hasattr(self.model1, 'id'))
        self.assertIsInstance(self.model1.id, str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_attr_created_at(self):
        """Tests the created_at attribute of instance"""
        self.assertTrue(hasattr(self.model1, 'created_at'))
        self.assertIsInstance(self.model1.created_at, datetime)

    def test_attr_updated_at(self):
        """Tests the updated_at attribute of instance"""
        self.assertTrue(hasattr(self.model1, 'updated_at'))
        self.assertIsInstance(self.model1.updated_at, datetime)

    def test_method_str(self):
        """Tests the str method"""
        expected_string = f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}"
        actual_string = str(self.model1)
        self.assertMultiLineEqual(expected_string, actual_string)

    def test_method_save(self):
        """Tests the save public instance method"""

        # Check that created_at == updated_at when instance is created
        self.assertEqual(self.model1.created_at, self.model1.updated_at)

        # Check that created_at != updated_at after instance is updated
        self.model1.name = "Model 1"
        self.model1.save()
        self.assertNotEqual(self.model1.created_at, self.model1.updated_at)

        # Check that updated_at > created_at after instance is updated
        self.assertGreaterEqual(self.model1.updated_at, self.model1.created_at)

    def test_method_to_dict(self):
        """Tests the to_dict public instance method"""


    def teardown(self):
        """Dispose test object"""
        self.model1.dispose()
        self.model2.dispose()

if __name__ == "__main__":
    unittest.main()
