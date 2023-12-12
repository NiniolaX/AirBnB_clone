#!/usr/bin/python3

"""Test module for Place class."""


import unittest
import io
import sys

from models.place import Place
from datetime import datetime


class TestInitialization(unittest.TestCase):
    """Tests initialization of the Place class."""

    def test_initialization(self):
        """Testing initialization of the Place class."""

        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

        place = Place("name")
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        place.name = "John"
        place_dict = place.to_dict()
        place1 = Place(**place_dict)
        self.assertIsInstance(place1, Place)
        self.assertIsInstance(place1.id, str)
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)
        self.assertEqual(place.id, place1.id)
        self.assertEqual(place.name, place1.name)
        self.assertEqual(place.created_at, place1.created_at)
        self.assertEqual(place.updated_at, place1.updated_at)
        self.assertFalse(isinstance(getattr(place, "__class__", None), str))

        place1 = Place(
            id=place_dict["id"], name="James",
            created_at=place_dict["created_at"])
        self.assertIsInstance(place1, Place)
        self.assertIsInstance(place1.id, str)
        self.assertIsInstance(place1.created_at, datetime)
        self.assertTrue(
            isinstance(getattr(place1, "updated_at", None), datetime))
        self.assertEqual(place.id, place1.id)
        self.assertNotEqual(place.name, place1.name)
        self.assertEqual(place.created_at, place1.created_at)
        self.assertNotEqual(
            getattr(place1, "updated_at", None), place.updated_at)

        with self.assertRaises(ValueError) as ctx:
            place1 = Place(
                id=place_dict["id"], name="James",
                created_at=place_dict["created_at"],
                updated_at="this is a bad date string")
        msg = str(ctx.exception)
        self.assertRegex(
            str(ctx.exception), msg)


class TestSaveInstanceMethod(unittest.TestCase):
    """Tests the 'save' instance method of the Place class."""

    def test_save_instance_method(self):
        """Test the 'save' instance method of the Place class."""
        place = Place()
        date1 = place.updated_at
        place.save()
        date2 = place.updated_at
        self.assertNotEqual(date1, date2)


class TestToDictInstanceMethod(unittest.TestCase):
    """Tests the 'to_dict' instance method of the Place class."""

    def test_to_dict_instance_method(self):
        """Test the 'to_dict' instance method of the Place class."""
        place = Place()
        place_dict = place.to_dict()
        place_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(place_dict, dict)
        self.assertSetEqual(set(place_dict.keys()), place_dict_keys)
        self.assertIsInstance(place_dict["id"], str)
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

        place = Place()
        place.name = "John"
        place.age = 50
        place_dict = place.to_dict()
        place_dict_keys = {
            "__class__", "id", "created_at", "updated_at", "name", "age"}
        self.assertIsInstance(place_dict, dict)
        self.assertSetEqual(set(place_dict.keys()), place_dict_keys)
        self.assertIsInstance(place_dict["name"], str)
        self.assertIsInstance(place_dict["age"], int)

        with self.assertRaises(TypeError):
            place_dict = place.to_dict("argument")


class TestStrRepresentation(unittest.TestCase):
    """Tests the '__str__' function of the Place class."""

    def test_str_representation(self):
        """Test the '__str__' function of the Place class."""
        place = Place()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(place)

        place_str = new_stdout.getvalue()
        self.assertIn("[Place]", place_str)
        self.assertIn("'id': ", place_str)
        self.assertIn("'created_at': datetime.datetime", place_str)
        self.assertIn("'updated_at': datetime.datetime", place_str)
        self.assertEqual(
            f"[{place.__class__.__name__}] ({place.id}) {place.__dict__}\n",
            place_str)
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
