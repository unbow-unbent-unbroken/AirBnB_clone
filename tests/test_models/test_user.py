#!/usr/bin/python3
""" Defines unittests for models/user.py. """

import os
import unittest
from time import sleep
from datetime import datetime
from models.user import User


class TestUserInit(unittest.TestCase):
    def test_obj_type(self):
        """Verify that the object is an instance of User."""
        obj = User()
        self.assertEqual(type(obj), User)

    def test_multiple_instances(self):
        """Test handling multiple instances."""
        user1 = User()
        user2 = User()

        self.assertNotEqual(user1.id, user2.id)
        user1.name = "User1"
        user2.name = "User2"

        self.assertEqual(user1.name, "User1")
        self.assertEqual(user2.name, "User2")

    def test_no_class_attribute(self):
        """Test if __class__ attribute is not set in the __init__ method."""
        kwargs = {
            'id': 'test_id',
            'created_at': '2024-02-11T12:34:56',
            'updated_at': '2024-02-11T12:45:00',
            'custom_field': 'custom_value',
            '__class__': 'ShouldNotBeSet'
        }

        instance = User(**kwargs)
        self.assertNotIn('__class__', instance.__dict__)

    def test_id_type(self):
        """Verify that the 'id' attribute is of type str."""
        obj = User()
        self.assertEqual(type(obj.id), str)

    def test_created_type(self):
        """Verify that the 'created_at' attribute is of type datetime."""
        obj = User()
        self.assertEqual(type(obj.created_at), datetime)

    def test_updated_type(self):
        """Verify that the 'updated_at' attribute is of type datetime."""
        obj = User()
        self.assertEqual(type(obj.updated_at), datetime)

    def test_different_id(self):
        """Verify that two instances have different 'id' values."""
        x = User()
        y = User()
        self.assertNotEqual(x.id, y.id)

    def test_public_attribute(self):
        """Test case to check if setting a public attribute works"""
        instance = User()
        instance.name = "godie"
        self.assertEqual(instance.name, "godie")

    def test_update_at(self):
        """Verify that 'updated_at' changes after updating
         attribute and saving."""
        x = User()
        sleep(1)
        x.name = "godie"
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_update_attributes(self):
        """Verify that attributes can be updated and saved."""
        kwargs = {
            'name': 'Godfrey',
            'age': 23,
        }

        obj = User(**kwargs)
        self.assertEqual(obj.name, "Godfrey")
        obj.name = "Done"
        self.assertEqual(obj.name, "Done")

    def test_created_different_time(self):
        """Verify that 'created_at' times are different for
            two instances created with a time gap.
        """
        x = User()
        sleep(1)
        y = User()
        self.assertNotEqual(x.created_at, y.created_at)

    def test_updated_different_time(self):
        """Verify that 'updated_at' times are different after saving
         two instances with different changes.
         """
        x = User()
        y = User()
        x.name = "test"
        x.save()
        y.name = "pass"
        y.save()
        self.assertNotEqual(x.updated_at, y.updated_at)

    def test_create_with_kwargs(self):
        """Test case when kwargs is provided"""
        kwargs = {
            'id': 'test_id',
            'created_at': '2024-02-11T12:34:56',
            'updated_at': '2024-02-11T12:45:00',
            'custom_field': 'custom_value'
        }

        instance = User(**kwargs)

        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_field, 'custom_value')
        self.assertEqual(instance.created_at,
                         datetime.fromisoformat('2024-02-11T12:34:56'))
        self.assertEqual(instance.updated_at,
                         datetime.fromisoformat('2024-02-11T12:45:00'))

    def test_create_with_kwargs_type(self):
        """Test creating a new instance"""
        kwargs = {
            'name': 'Godfrey',
            'age': 23,
        }
        obj = User(**kwargs)
        self.assertEqual(type(obj.age), int)
        self.assertEqual(type(obj.name), str)

    def test_kwargs_values(self):
        """Test kwargs values"""
        kwargs = {
            'name': 'Godfrey',
            'age': 23,
        }
        obj = User(**kwargs)
        self.assertEqual(obj.name, "Godfrey")
        self.assertEqual(obj.age, 23)

    def test_print_class(self):
        """Test case to check if the class can be printed"""
        instance = User()
        printed_output = str(instance)
        self.assertIn("User", printed_output)
        self.assertIn("id", printed_output)
        self.assertIn("created_at", printed_output)
        self.assertIn("updated_at", printed_output)

    def test_docstring(self):
        """Test case to check if the class contains a docstring"""
        self.assertIsNotNone(User.__doc__)
        self.assertNotEqual(User.__doc__, "")

    def test_to_dict_method(self):
        """Test case for the to_dict method"""
        instance = User()
        instance.name = "godie"
        instance.created_at = datetime(2024, 2,
                                       11, 12, 34, 56)
        instance.updated_at = datetime(2024, 2,
                                       11, 12, 45, 0)

        expected_dict = {
            'id': instance.id,
            'created_at': '2024-02-11T12:34:56',
            'updated_at': '2024-02-11T12:45:00',
            'name': 'godie',
            '__class__': 'User'
        }

        self.assertEqual(instance.to_dict(), expected_dict)

    def test_to_dict_default_values(self):
        """Test case for to_dict method with default values"""
        instance = User()

        expected_dict = {
            'id': instance.id,
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
            '__class__': 'User'
        }

        self.assertEqual(instance.to_dict(), expected_dict)

    def test_to_dict_with_custom_attributes(self):
        """Test case for to_dict method with custom attributes"""
        instance = User()
        instance.custom_field = 'custom_value'

        expected_dict = {
            'id': instance.id,
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
            'custom_field': 'custom_value',
            '__class__': 'User'
        }

        self.assertEqual(instance.to_dict(), expected_dict)


class TestUserAttributes(unittest.TestCase):
    def test_default_attribute_values(self):
        """Test that default attribute values are empty strings."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        """Test that attribute types are as expected."""
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_attribute_assignment(self):
        """Test assigning values to attributes."""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_attribute_assignment_type(self):
        """Test assigning values of correct types to attributes."""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_to_dict_with_attributes(self):
        """Test to_dict method with custom attributes."""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        expected_dict = {
            'id': user.id,
            'created_at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat(),
            'email': 'user@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
            '__class__': 'User'
        }

        self.assertEqual(user.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
