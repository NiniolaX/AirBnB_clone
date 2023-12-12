#!/usr/bin/python3

""" Test module for Review class """


import unittest
import io
import sys

from models.review import Review
from datetime import datetime


class TestReviewInitialization(unittest.TestCase):
    """ A TestCase class that tests the Review class """

    def test_initialization(self):
        """ testing initialization of the Review class """
        model = Review()
        self.assertIsInstance(model, Review)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model = Review("name")
        self.assertIsInstance(model, Review)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.place_id, str)
        self.assertIsInstance(model.user_id, str)
        self.assertIsInstance(model.text, str)
        self.assertEqual(model.place_id, "")
        self.assertEqual(model.user_id, "")
        self.assertEqual(model.text, "")

        model.name = "John"
        model_dict = model.to_dict()
        model1 = Review(**model_dict)
        self.assertIsInstance(model1, Review)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)
        self.assertEqual(model.id, model1.id)
        self.assertEqual(model.name, model1.name)
        self.assertEqual(model.created_at, model1.created_at)
        self.assertEqual(model.updated_at, model1.updated_at)
        self.assertFalse(isinstance(getattr(model, "__class__", None), str))

        model1 = Review(
            id=model_dict["id"], name="James",
            created_at=model_dict["created_at"])
        self.assertIsInstance(model1, Review)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertTrue(
            isinstance(getattr(model1, "updated_at", None), datetime))
        self.assertEqual(model.id, model1.id)
        self.assertNotEqual(model.name, model1.name)
        self.assertEqual(model.created_at, model1.created_at)
        self.assertNotEqual(
            getattr(model1, "updated_at", None), model.updated_at)

        with self.assertRaises(ValueError) as review_error:
            model1 = Review(
                id=model_dict["id"], name="James",
                created_at=model_dict["created_at"],
                updated_at="unique date string")
        msg = str(review_error.exception)
        self.assertRegex(
            str(review_error.exception), msg)


class TestReviewSaveInstanceMethod(unittest.TestCase):
    """Tests the 'save' instance method of the Review class."""

    def test_save_instance_method(self):
        """Test the 'save' instance method of the Review class."""
        model = Review()
        date1 = model.updated_at
        model.save()
        date2 = model.updated_at
        self.assertNotEqual(date1, date2)


class TestReviewToDictInstanceMethod(unittest.TestCase):
    """Tests the 'to_dict' instance method of the Review class."""

    def test_to_dict_instance_method(self):
        """Test the 'to_dict' instance method of the Review class."""
        model = Review()
        model_dict = model.to_dict()
        model_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(model_dict, dict)
        self.assertSetEqual(set(model_dict.keys()), model_dict_keys)
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

        model = Review()
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


class TestReviewStrRepresentation(unittest.TestCase):
    """Tests the '__str__' function of the Review class."""

    def test_str_representation(self):
        """Test the '__str__' function of the Review class."""
        model = Review()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(model)

        review_str = new_stdout.getvalue()
        self.assertIn("[Review]", review_str)
        self.assertIn("'id': ", review_str)
        self.assertIn("'created_at': datetime.datetime", review_str)
        self.assertIn("'updated_at': datetime.datetime", review_str)
        self.assertEqual(
            f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}\n",
            review_str)
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
