#!/usr/bin/python3

""" Test module for State class """


import unittest
import io
import sys

from models.state import State
from datetime import datetime


class TestStateInitialization(unittest.TestCase):
    """ A TestCase class that tests the initialization of the State class """

    def test_initialization(self):
        """ testing initialization of the State class """
        model = State()
        self.assertIsInstance(model, State)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model = State("name")
        self.assertIsInstance(model, State)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.name, str)
        self.assertEqual(model.name, "")

        model.name = "John"
        model_dict = model.to_dict()
        model1 = State(**model_dict)
        self.assertIsInstance(model1, State)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)
        self.assertEqual(model.id, model1.id)
        self.assertEqual(model.name, model1.name)
        self.assertEqual(model.created_at, model1.created_at)
        self.assertEqual(model.updated_at, model1.updated_at)
        self.assertFalse(isinstance(getattr(model, "__class__", None), str))

        model1 = State(
            id=model_dict["id"], name="James",
            created_at=model_dict["created_at"])
        self.assertIsInstance(model1, State)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertTrue(
            isinstance(getattr(model1, "updated_at", None), datetime))
        self.assertEqual(model.id, model1.id)
        self.assertNotEqual(model.name, model1.name)
        self.assertEqual(model.created_at, model1.created_at)
        self.assertNotEqual(
            getattr(model1, "updated_at", None), model.updated_at)

        with self.assertRaises(ValueError) as state_error:
            model1 = State(
                id=model_dict["id"], name="James",
                created_at=model_dict["created_at"],
                updated_at="unique date string")
        msg = str(state_error.exception)
        self.assertRegex(
            str(state_error.exception), msg)


class TestStateSaveInstanceMethod(unittest.TestCase):
    """A TestCase class, tests the save instance method of the State class"""

    def test_save_instance_method(self):
        """ test the save instance method of the State class """
        model = State()
        date1 = model.updated_at
        model.save()
        date2 = model.updated_at
        self.assertNotEqual(date1, date2)


class TestStateToDictInstanceMethod(unittest.TestCase):
    """TestCase class, tests the to_dict instance method of the State Class"""

    def test_to_dict_instance_method(self):
        """ test the to_dict instance method of the State Class """
        model = State()
        m_dict = model.to_dict()
        m_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(m_dict, dict)
        self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
        self.assertIsInstance(m_dict["id"], str)
        self.assertIsInstance(m_dict["created_at"], str)
        self.assertIsInstance(m_dict["updated_at"], str)

        model = State()
        model.name = "John"
        model.age = 50
        m_dict = model.to_dict()
        m_dict_keys = {
            "__class__", "id", "created_at", "updated_at", "name", "age"}
        self.assertIsInstance(m_dict, dict)
        self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
        self.assertIsInstance(m_dict["name"], str)
        self.assertIsInstance(m_dict["age"], int)

        with self.assertRaises(TypeError):
            m_dict = model.to_dict("argument")


class TestStateStrRepresentation(unittest.TestCase):
    """ A TestCase class that tests the __str__ function of the State """

    def test_str_representation(self):
        """ test the __str__ function of the State """
        model = State()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(model)

        m_str = new_stdout.getvalue()
        self.assertIn("[State]", m_str)
        self.assertIn("'id': ", m_str)
        self.assertIn("'created_at': datetime.datetime", m_str)
        self.assertIn("'updated_at': datetime.datetime", m_str)
        self.assertEqual(
            f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}\n",
            m_str)
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
