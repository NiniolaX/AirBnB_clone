#!/usr/bin/python3
"""Unit test for BaseModel class."""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelClass(unittest.TestCase):
    """Tests the BaseModel class of the models module class"""

    def setUp(self):
        """Sets up BaseModel object for testing"""
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """Dispose test object"""
        del self.model1
        del self.model2

    def test_constructor(self):
        """Tests the class constructor"""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(self.model2, BaseModel)

        # Test that object re-creation from its dict representation works:

        # Generate dictionary representation of original object (self.model1)
        actual_obj_dict = self.model1.to_dict()

        # Re-create original object from its dictionary representation
        recreated_obj = BaseModel(**actual_obj_dict)

        # Check that str represantations of actual obj and re-cereated are same
        self.assertEqual(str(recreated_obj), str(self.model1))

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
        expected_str = f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}"
        actual_str = str(self.model1)
        self.assertMultiLineEqual(expected_str, actual_str)

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
        expected_dict = self.model1.to_dict()

        # Check that only instance attributes set are in expected_dict
        self.assertNotIn('unset_attr', expected_dict)

        # Check that __class__ key and value exists
        self.assertIn('__class__', expected_dict)

        # Check that value of __class__ key is class name of object
        self.assertEqual(expected_dict['__class__'], 'BaseModel')

        # Check that created_at and updated_at attr of dict are string objects
        self.assertIsInstance(expected_dict['created_at'], str)
        self.assertIsInstance(expected_dict['updated_at'], str)

        # Check that created_at and updated_at attr of dict are in ISO format
        def is_ISO_format(datetime_str):
            """Attempt to parse a string into datetime object in ISO format"""
            try:
                datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f")
                return True
            except ValueError:
                return False

        self.assertTrue(is_ISO_format(expected_dict['created_at']))
        self.assertTrue(is_ISO_format(expected_dict['updated_at']))


if __name__ == "__main__":
    unittest.main()
