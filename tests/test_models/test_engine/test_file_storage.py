#!/usr/bin/python3

"""This module contains test cases for the self.storage engine."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestStorageEngine(unittest.TestCase):
    """Tests the file_self.storage module of 'engine' package."""

    def setUp(self):
        """Sets up a FileStorage object for testing"""
        self.file_path = "file.json"
        # Delete storage file if exists
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Create objects for testing
        self.test_obj = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """Disposes test objects"""
        del self.test_obj
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_private_attr_file_path(self):
        """Tests private class attribute file_path"""
        # Check that storage file exists
        self.storage.save()  # since save() creates file if it doesn't exist
        self.assertTrue(os.path.exists(self.file_path))

    def test_attr_objects(self):
        """Tests the private class attribute objects"""
        # Check that __objects attribute is a dict
        objects = self.storage.all()  # since all() returns __objects
        self.assertIsInstance(objects, dict)

    def test_method_all(self):
        """Tests the all() method"""
        # Test that return value of all is a dictionary
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        initial_obj_count = len(all_objs)

        # Tests that all() updates with each new object
        new_obj = BaseModel()
        all_objs = self.storage.all()
        self.assertIn(new_obj, all_objs.values())
        self.assertTrue(len(all_objs) == initial_obj_count + 1)

        new_obj2 = BaseModel()
        all_objs = self.storage.all()
        self.assertIn(new_obj, all_objs.values())
        self.assertTrue(len(all_objs) == initial_obj_count + 2)

    def test_method_new(self):
        """Tests the 'new' method"""
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
        """Tests the 'save' method"""
        # Check that file is created on call to save()
        self.assertFalse(os.path.exists(self.file_path))
        self.storage.save()  # Saving BaseModel object created in setUp()...
        self.assertTrue(os.path.exists(self.file_path))

        # Check that saved object exists in file
        saved_obj_key = f"BaseModel.{self.test_obj.id}"

        with open(self.file_path, 'r') as file:
            file_content = file.read()

        self.assertIn(saved_obj_key, file_content)

    def test_method_reload(self):
        """Tests the 'reload' method"""
        actual_obj = self.test_obj
        self.storage.save()  # Saving actual_obj ...
        self.storage.reload()

        # Getting reloaded object
        all_reloaded_objs = self.storage.all()
        for key in all_reloaded_objs.keys():
            if key == f"BaseModel.{actual_obj.id}":
                reloaded_obj = all_reloaded_objs[key]

        self.assertEqual(actual_obj.id, reloaded_obj.id)
        self.assertEqual(actual_obj.created_at, reloaded_obj.created_at)
        self.assertEqual(actual_obj.updated_at, reloaded_obj.updated_at)
