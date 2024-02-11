#!/usr/bin/python3
"""Defines unittests for models/state.py."""

import os
import unittest
from time import sleep
from datetime import datetime
from models.state import State


class TestState_obj_init(unittest.TestCase):
    def test_obj_type(self):
        """Verify that the object is an instance of State."""
        obj = State()
        self.assertEqual(type(obj), State)

    def test_multiple_instances(self):
        """Test handling multiple instances."""
        state1 = State()
        state2 = State()

        self.assertNotEqual(state1.id, state2.id)
        state1.name = "State1"
        state2.name = "State2"

        self.assertEqual(state1.name, "State1")
        self.assertEqual(state2.name, "State2")

    def test_no_class_attribute(self):
        """Test if __class__ attribute is not set in
        the __init__ method."""
        kwargs = {
            'id': 'test_id',
            'created_at': '2024-02-11T12:34:56',
            'updated_at': '2024-02-11T12:45:00',
            'custom_field': 'custom_value',
            '__class__': 'ShouldNotBeSet'
        }

        instance = State(**kwargs)
        self.assertNotIn('__class__', instance.__dict__)

    def test_id_type(self):
        """Verify that the 'id' attribute is of type str."""
        obj = State()
        self.assertEqual(type(obj.id), str)

    def test_created_type(self):
        """Verify that the 'created_at' attribute is of type datetime."""
        obj = State()
        self.assertEqual(type(obj.created_at), datetime)

    def test_updated_type(self):
        """Verify that the 'updated_at' attribute is of type datetime."""
        obj = State()
        self.assertEqual(type(obj.updated_at), datetime)

    def test_different_id(self):
        """Verify that two instances have different 'id' values."""
        x = State()
        y = State()
        self.assertNotEqual(x.id, y.id)

    def test_public_attribute(self):
        """Test case to check if setting a public attribute works"""
        instance = State()
        instance.name = "California"
        self.assertEqual(instance.name, "California")

    def test_update_at(self):
        """Verify that 'updated_at' changes after updating
            an attribute and saving."""
        x = State()
        sleep(1)
        x.name = "New York"
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_update_attributes(self):
        """Verify that attributes can be updated and saved."""
        kwargs = {
            'name': 'Texas',
            'population': 29000000,
        }

        obj = State(**kwargs)
        self.assertEqual(obj.name, "Texas")
        obj.name = "Florida"
        self.assertEqual(obj.name, "Florida")

    def test_created_different_time(self):
        """Verify that 'created_at' times are different for
            two instances created with a time gap.
        """
        x = State()
        sleep(1)
        y = State()
        self.assertNotEqual(x.created_at, y.created_at)

    def test_updated_different_time(self):
        """Verify that 'updated_at' times are different after saving
         two instances with different changes.
         """
        x = State()
        y = State()
        x.name = "Arizona"
        x.save()
        y.name = "Nevada"
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

        instance = State(**kwargs)

        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_field, 'custom_value')
        self.assertEqual(instance.created_at,
                         datetime.fromisoformat('2024-02-11T12:34:56'))
        self.assertEqual(instance.updated_at,
                         datetime.fromisoformat('2024-02-11T12:45:00'))

    def test_create_with_kwargs_type(self):
        """Test creating a new instance"""
        kwargs = {
            'name': 'California',
            'population': 39000000,
        }
        obj = State(**kwargs)
        self.assertEqual(type(obj.population), int)
        self.assertEqual(type(obj.name), str)

    def test_kwargs_values(self):
        """Test kwargs values"""
        kwargs = {
            'name': 'California',
            'population': 39000000,
        }
        obj = State(**kwargs)
        self.assertEqual(obj.name, 'California')
        self.assertEqual(obj.population, 39000000)


if __name__ == "__main__":
    unittest.main()
