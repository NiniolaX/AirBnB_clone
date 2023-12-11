#!/usr/bin/python3

"""Test module for base_model module"""


from models.base_model import BaseModel
import unittest
from datetime import datetime
import io
import sys


class TestBaseModel(unittest.TestCase):
    """Unittests to test the base_model class"""

    def test_model_initialization(self):
        """test base_model initialization of values"""
        new_model = BaseModel()
        # check if it's an instance
        self.assertIsInstance(new_model, BaseModel)
        # check the model id
        self.assertIsInstance(new_model.id, str)
        # check time created
        self.assertIsInstance(new_model.created_at, datetime)
        # check time updated
        self.assertIsInstance(new_model.updated_at, datetime)

        model = BaseModel()
        model_dict = model.to_dict()
        model_two = BaseModel(**model_dict)
        self.assertIsInstance(model_two, BaseModel)
        self.assertIsInstance(model_two.id, str)
        self.assertIsInstance(model_two.created_at, datetime)
        self.assertIsInstance(model_two.updated_at, datetime)
        self.assertEqual(model.id, model_two.id)
        self.assertEqual(model.created_at, model_two.created_at)
        self.assertEqual(model.updated_at, model.updated_at)
        self.assertFalse(isinstance(getattr(model, "__class__", None), str))

        model = BaseModel("last_name")
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model_two = BaseModel(
            id=model_dict["id"], name="James",
            created_at=model_dict["created_at"])
        self.assertIsInstance(model_two, BaseModel)
        self.assertIsInstance(model_two.id, str)
        self.assertIsInstance(model_two.created_at, datetime)
        self.assertTrue(
                isinstance(getattr(model_two, "updated_at", None), datetime))
        self.assertNotEqual(model.id, model_two.id)
        self.assertNotEqual(model.created_at, model_two.created_at)
        self.assertNotEqual(
            getattr(model_two, "updated_at", None), model.updated_at)

        with self.assertRaises(ValueError) as ctx:
            model_two = BaseModel(
                id=model_dict["id"], name="James",
                created_at=model_dict["created_at"],
                updated_at="bad date str")
        msg = str(ctx.exception)
        self.assertRegex(
            str(ctx.exception), msg)

        def test_str_repr(self):
            """ tests the str func repere of the base_model"""

            my_model = BaseModel()
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            print(model)

            m_str = new_stdout.getvalue()
            self.assertIn("[BaseModel]", m_str)
            self.assertIn("'id': ", m_str)
            self.assertIn("'created_at': datetime.datetime", m_str)
            self.assertIn("'updated_at': datetime.datetime", m_str)
            self.assertEqual(
                f"[{my_model.__class__.__name__}]({model.id}) "
                "{my_model.__dict__}\n",
                m_str)
            sys.stdout = sys.__stdout__

        def test_save_instance_method(self):
            """test the save instance method of base_model class """

            my_model = BaseModel()
            date1 = my_model.updated_at
            my_model.save()
            date2 = my_model.updated_at
            self.assertNotEqual(date1, date2)

        def test_to_dict_instance_method(self):
            """ test to_dict instance method of Basemodel class"""

            my_model = BaseModel()
            m_dict = my_model.to_dict()
            m_dict_keys = {"__class__", "id", "created_at", "updated_at"}
            self.assertIsInstance(m_dict, dict)
            self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
            self.assertIsInstance(m_dict["id"], str)
            self.assertIsInstance(m_dict["created_at"], str)
            self.assertIsInstance(m_dict["updateed_at"], str)

            my_model = BaseModel()
            my_model.name = "John"
            my_model.age = 293
            m_dict = my_model.to_dict()
            m_dict_keys = {
                "__class__", "created_at",
                "updateed_at", "name", "age"
                }
            self.assertIsInstance(m_dict, dict)
            self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
            self.assertIsInstance(m_dict["name"], str)
            self.assertIsInstance(m_dict["age"], int)

            with self.assertRaises(TypeError):
                m_dict = my_model.to_dict("arg")


if __name__ == '__main__':
    unittest.main()
    BaseModel()
