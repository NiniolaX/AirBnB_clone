#!/usr/bin/python3

"""Test module for User class."""


import unittest
import io
import sys

from models.user import User
from datetime import datetime


class TestUserInitialization(unittest.TestCase):
    """A TestCase class for the User class."""

    def test_initialization(self):
        """Test for initialization of the User class."""

        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        user = User("name")
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

        user.name = "John"
        user_dict = user.to_dict()
        user1 = User(**user_dict)
        self.assertIsInstance(user1, User)
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime)
        self.assertIsInstance(user1.updated_at, datetime)
        self.assertEqual(user.id, user1.id)
        self.assertEqual(user.name, user1.name)
        self.assertEqual(user.created_at, user1.created_at)
        self.assertEqual(user.updated_at, user1.updated_at)
        self.assertFalse(isinstance(getattr(user, "__class__", None), str))

        user1 = User(
            id=user_dict["id"], name="James",
            created_at=user_dict["created_at"])
        self.assertIsInstance(user1, User)
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime)
        self.assertTrue(
            isinstance(getattr(user1, "updated_at", None), datetime))
        self.assertEqual(user.id, user1.id)
        self.assertNotEqual(user.name, user1.name)
        self.assertEqual(user.created_at, user1.created_at)
        self.assertNotEqual(
            getattr(user1, "updated_at", None), user.updated_at)

        with self.assertRaises(ValueError) as ctx:
            user1 = User(
                id=user_dict["id"], name="James",
                created_at=user_dict["created_at"],
                updated_at="this is a bad date string")
        msg = str(ctx.exception)
        self.assertRegex(
            str(ctx.exception), msg)


class TestUserSaveInstanceMethod(unittest.TestCase):
    """Tests the 'save' instance method of the User class."""

    def test_save_instance_method(self):
        """Test the 'save' instance method of the User class."""
        user = User()
        date1 = user.updated_at
        user.save()
        date2 = user.updated_at
        self.assertNotEqual(date1, date2)


class TestUserToDictInstanceMethod(unittest.TestCase):
    """Tests the 'to_dict' instance method of the User class."""

    def test_to_dict_instance_method(self):
        """Test the 'to_dict' instance method of the User class."""
        user = User()
        user_dict = user.to_dict()
        user_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(user_dict, dict)
        self.assertSetEqual(set(user_dict.keys()), user_dict_keys)
        self.assertIsInstance(user_dict["id"], str)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

        user = User()
        user.name = "John"
        user.age = 50
        user_dict = user.to_dict()
        user_dict_keys = {
            "__class__", "id", "created_at", "updated_at", "name", "age"}
        self.assertIsInstance(user_dict, dict)
        self.assertSetEqual(set(user_dict.keys()), user_dict_keys)
        self.assertIsInstance(user_dict["name"], str)
        self.assertIsInstance(user_dict["age"], int)

        with self.assertRaises(TypeError):
            user_dict = user.to_dict("argument")


class TestUserStrRepresentation(unittest.TestCase):
    """Tests the '__str__' function of the User class."""

    def test_str_representation(self):
        """Test the '__str__' function of the User class."""
        user = User()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(user)

        user_str = new_stdout.getvalue()
        self.assertIn("[User]", user_str)
        self.assertIn("'id': ", user_str)
        self.assertIn("'created_at': datetime.datetime", user_str)
        self.assertIn("'updated_at': datetime.datetime", user_str)
        self.assertEqual(
            f"[{user.__class__.__name__}] ({user.id}) {user.__dict__}\n",
            user_str)
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
