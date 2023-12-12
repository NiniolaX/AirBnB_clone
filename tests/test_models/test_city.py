#!/usr/bin/python3

"""Test module for City class."""

import unittest
import io
import sys

from models.city import City
from datetime import datetime


class TestCityInitialization(unittest.TestCase):
    """A TestCase class that tests the City class."""

    def test_initialization(self):
        """Test the initialization of the City class."""

        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

        city = City("name")
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

        city.name = "John"
        city_dict = city.to_dict()
        city1 = City(**city_dict)
        self.assertIsInstance(city1, City)
        self.assertIsInstance(city1.id, str)
        self.assertIsInstance(city1.created_at, datetime)
        self.assertIsInstance(city1.updated_at, datetime)
        self.assertEqual(city.id, city1.id)
        self.assertEqual(city.name, city1.name)
        self.assertEqual(city.created_at, city1.created_at)
        self.assertEqual(city.updated_at, city1.updated_at)
        self.assertFalse(isinstance(getattr(city, "__class__", None), str))

        city1 = City(
            id=city_dict["id"], name="James",
            created_at=city_dict["created_at"])
        self.assertIsInstance(city1, City)
        self.assertIsInstance(city1.id, str)
        self.assertIsInstance(city1.created_at, datetime)
        self.assertTrue(
            isinstance(getattr(city1, "updated_at", None), datetime))
        self.assertEqual(city.id, city1.id)
        self.assertNotEqual(city.name, city1.name)
        self.assertEqual(city.created_at, city1.created_at)
        self.assertNotEqual(
            getattr(city1, "updated_at", None), city.updated_at)

        with self.assertRaises(ValueError) as ctx:
            city1 = City(
                id=city_dict["id"], name="James",
                created_at=city_dict["created_at"],
                updated_at="this is a bad date string")
        msg = str(ctx.exception)
        self.assertRegex(
            str(ctx.exception), msg)


class TestCitySaveInstanceMethod(unittest.TestCase):
    """Tests the 'save' instance method of the City class."""

    def test_save_instance_method(self):
        """Test the 'save' instance method of the City class."""
        city = City()
        date1 = city.updated_at
        city.save()
        date2 = city.updated_at
        self.assertNotEqual(date1, date2)


class TestCityToDictInstanceMethod(unittest.TestCase):
    """Tests the 'to_dict' instance method of the City class."""

    def test_to_dict_instance_method(self):
        """Test the 'to_dict' instance method of the City class."""
        city = City()
        city_dict = city.to_dict()
        city_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(city_dict, dict)
        self.assertSetEqual(set(city_dict.keys()), city_dict_keys)
        self.assertIsInstance(city_dict["id"], str)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

        city = City()
        city.name = "John"
        city.age = 50
        city_dict = city.to_dict()
        city_dict_keys = {
            "__class__", "id", "created_at", "updated_at", "name", "age"}
        self.assertIsInstance(city_dict, dict)
        self.assertSetEqual(set(city_dict.keys()), city_dict_keys)
        self.assertIsInstance(city_dict["name"], str)
        self.assertIsInstance(city_dict["age"], int)

        with self.assertRaises(TypeError):
            city_dict = city.to_dict("argument")


class TestCityStrRepresentation(unittest.TestCase):
    """Tests the '__str__' function of the City class."""

    def test_str_representation(self):
        """Test the '__str__' function of the City class."""
        city = City()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(city)

        city_str = new_stdout.getvalue()
        self.assertIn("[City]", city_str)
        self.assertIn("'id': ", city_str)
        self.assertIn("'created_at': datetime.datetime", city_str)
        self.assertIn("'updated_at': datetime.datetime", city_str)
        self.assertEqual(
            f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}\n",
            city_str)
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
