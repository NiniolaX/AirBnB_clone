#!/usr/bin/python3

"""Test module for BaseModel class."""


import unittest
import io
import sys

from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelInitialization(unittest.TestCase):
    """A TestCase class that tests the BaseModel class initialization."""

    def test_initialization(self):
        """Test the initialization of the BaseModel class."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model = BaseModel()
        model_dict = model.to_dict()
        model1 = BaseModel(**model_dict)
        self.assertIsInstance(model1, BaseModel)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)
        self.assertEqual(model.id, model1.id)
        self.assertEqual(model.created_at, model1.created_at)
        self.assertEqual(model.updated_at, model.updated_at)
        self.assertFalse(isinstance(getattr(model, "__class__", None), str))

        model = BaseModel("name")
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model1 = BaseModel(
            id=model_dict["id"], name="James",
            created_at=model_dict["created_at"])
        self.assertIsInstance(model1, BaseModel)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertTrue(
                isinstance(getattr(model1, "updated_at", None), datetime))
        self.assertNotEqual(model.id, model1.id)
        self.assertNotEqual(model.created_at, model1.created_at)
        self.assertNotEqual(
            getattr(model1, "updated_at", None), model.updated_at)

        with self.assertRaises(ValueError) as ctx:
            model1 = BaseModel(
                id=model_dict["id"], name="James",
                created_at=model_dict["created_at"],
                updated_at="this is a bad date string")
        msg = str(ctx.exception)
        self.assertRegex(
            str(ctx.exception), msg)

    def test_str_representation(self):
        """Test the __str__ function of the BaseModel."""
        model = BaseModel()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(model)

        model_str = new_stdout.getvalue()
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("'id': ", model_str)
        self.assertIn("'created_at': datetime.datetime", model_str)
        self.assertIn("'updated_at': datetime.datetime", model_str)
        self.assertEqual(
            f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}\n",
            model_str)
        sys.stdout = sys.__stdout__


class TestBaseModelSaveInstanceMethod(unittest.TestCase):
    """Tests the 'save' instance method of the BaseModel class."""

    def test_save_instance_method(self):
        """Test the 'save' instance method of the BaseModel class."""
        model = BaseModel()
        date1 = model.updated_at
        model.save()
        date2 = model.updated_at
        self.assertNotEqual(date1, date2)


class TestBaseModelToDictInstanceMethod(unittest.TestCase):
    """Tests the 'to_dict' instance method of the BaseModel class."""

    def test_to_dict_instance_method(self):
        """Test the 'to_dict' instance method of the BaseModel class."""
        model = BaseModel()
        model_dict = model.to_dict()
        model_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(model_dict, dict)
        self.assertSetEqual(set(model_dict.keys()), model_dict_keys)
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

        model = BaseModel()
        model.name = "John"
        model.age = 50
        model_dict = model.to_dict()
        model_dict_keys = {
            "__class__", "id", "created_at", "updated_at", "name", "age"}
        self.assertIsInstance(model_dict, dict)
        self.assertSetEqual(set(model_dict.keys()), model_dict_keys)
        self.assertIsInstance(model_dict["name"], str)
        self.assertIsInstance(model_dict["age"], int)

        with self.assertRaises(TypeError):
            model_dict = model.to_dict("argument")


if __name__ == '__main__':
    unittest.main()
    BaseModel()
