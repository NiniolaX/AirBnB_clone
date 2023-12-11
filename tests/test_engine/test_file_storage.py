#!/usr/bin/python3

"""TestFileStorage class containing unittests."""

import uuid
import json
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestInstanceInitialization(unittest.TestCase):
    """Tests instance initialization."""

    def setUp(self):
        """Called before each task."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialize_instance(self):
        """Test instance initialization."""
        self.assertFalse(os.path.exists(self.file_path))
        storage = FileStorage()
        self.assertFalse(os.path.exists(self.file_path))


class TestAllInstanceMethod(unittest.TestCase):
    """Tests the 'all' instance method on the FileStorage instance."""

    def setUp(self):
        """Called before each task."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_instance_method(self):
        """Tests the 'all' instance method on the FileStorage instance."""
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        all_objects_len = len(all_objects)
        self.assertTrue(len(all_objects) == all_objects_len)

        model1 = BaseModel()
        all_objects = storage.all()
        self.assertTrue(len(all_objects) == 1 + all_objects_len)
        self.assertIn(model1, all_objects.values())

        model2 = BaseModel()
        all_objects = storage.all()
        self.assertTrue(len(all_objects) == 2 + all_objects_len)
        self.assertIn(model2, all_objects.values())

        with self.assertRaises(TypeError):
            storage.all("name")


class TestNewInstanceMethod(unittest.TestCase):
    """Tests the 'new' instance method on the FileStorage instance."""

    def setUp(self):
        """Called before each task."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new_instance_method(self):
        """Tests the 'new' instance method on the FileStorage instance."""
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        all_objects_len = len(all_objects)
        self.assertTrue(len(all_objects) == all_objects_len)

        model1 = BaseModel()
        all_objects = storage.all()
        self.assertTrue(len(all_objects) == 1 + all_objects_len)
        self.assertIn(model1, all_objects.values())

        model2 = BaseModel(**model1.to_dict())
        all_objects = storage.all()
        self.assertNotIn(model2, all_objects.values())
        self.assertTrue(len(all_objects) == 1 + all_objects_len)
        model2.id = str(uuid.uuid4())
        storage.new(model2)
        all_objects = storage.all()
        self.assertTrue(len(all_objects) == 2 + all_objects_len)
        self.assertIn(model2, all_objects.values())

        with self.assertRaises(TypeError):
            storage.new()

        with self.assertRaises(TypeError):
            storage.all(model1, model2)

        with self.assertRaises(AttributeError):
            storage.new("string")

        with self.assertRaises(AttributeError):
            storage.new(1)

        with self.assertRaises(AttributeError):
            storage.new({"a": 12})

        with self.assertRaises(AttributeError):
            storage.new((1, 2))

        with self.assertRaises(AttributeError):
            storage.new(1.5)


class TestSaveInstanceMethod(unittest.TestCase):
    """Tests the 'save' instance method on the FileStorage instance."""

    def setUp(self):
        """Called before each task."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_instance_method(self):
        """Tests the 'save' instance method on the FileStorage instance."""
        storage = FileStorage()
        all_objects = storage.all()
        all_objects_len = len(all_objects)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            storage.reload()

        self.assertTrue(all_objects_len == len(storage.all()))
        model1 = BaseModel()
        all_objects = storage.all()
        self.assertTrue(len(all_objects) == 1 + all_objects_len)
        self.assertIn(model1, all_objects.values())

        self.assertFalse(os.path.exists(self.file_path))
        storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        storage.reload()
        key = model1.__class__.__name__ + "." + model1.id
        self.assertEqual(model1.id, storage.all()[key].id)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            model1 = BaseModel()
            all_object = storage.all()
            self.assertTrue(len(all_objects) == 2 + all_objects_len)
            self.assertIn(model1, all_objects.values())

            self.assertFalse(os.path.exists(self.file_path))
            model1.save()
            self.assertTrue(os.path.exists(self.file_path))

            storage.reload()
            key = model1.__class__.__name__ + "." + model1.id
            self.assertEqual(model1.id, storage.all()[key].id)

            with self.assertRaises(TypeError):
                storage.reload(1.5)


if __name__ == "__main__":
    unittest.main()
