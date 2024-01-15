#!/usr/bin/python3

"""This module contains test cases for the self.storage engine."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestStorageEngine(unittest.TestCase):
    """Tests the file_self.storage module of 'engine' package."""

    def setUp(self):
        """Sets up a FileStorage object for testing"""
        self.test_obj = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """Disposes test objects"""
        del self.test_obj
        del self.storage

    def test_attr_file_path(self):
        """Tests that '__file_path' class attribute"""
        pass

    def test_attr_objects(self):
        """Tests the __objects class attribute"""
        # Check that __objects attribute is a dict
        objects = self.storage.all()  # since all() returns __objects
        self.assertIsInstance(objects, dict)

    def test_method_all(self):
        """Tests the all() method"""
        # Test that all() returns a dictionary
        returned_objs = self.storage.all()
        self.assertIsInstance(returned_objs, dict)

        # Tests that all() updates with each new object
        self.assertEqual(len(self.storage.all()), 0)

        self.storage.new(self.test_obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_method_new(self):
        """Tests the new() method"""
        new_obj = BaseModel()

        # Save new BaseModel object in __objects by calling new()
        self.storage.new(new_obj)

        # Test that __objects dict contains newly added object
        new_obj_dict = {}
        new_obj_key = f"{new_obj.__class__.__name__}.{new_obj.id}"
        new_obj_value = new_obj.to_dict()
        new_obj_dict[new_obj_key] = new_obj_value
        self.assertIn(new_obj_key, self.storage.all())

    def test_method_save(self):
        """Tests the save() method"""
