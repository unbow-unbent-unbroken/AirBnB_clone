#!/usr/bin/python3
""" Defines unittests for models/city.py. """

from time import sleep
import unittest
from datetime import datetime
from models.city import City


class TestCityInitialization(unittest.TestCase):
    def test_obj_type(self):
        """Verify that the object is an instance of City."""
        obj = City()
        self.assertEqual(type(obj), City)

    def test_multiple_instances(self):
        """Test handling multiple instances."""
        city1 = City()
        city2 = City()

        self.assertNotEqual(city1.id, city2.id)
        city1.name = "City1"
        city2.name = "City2"

        self.assertEqual(city1.name, "City1")
        self.assertEqual(city2.name, "City2")

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

        instance = City(**kwargs)
        self.assertNotIn('__class__', instance.__dict__)

    def test_id_type(self):
        """Verify that the 'id' attribute is of type str."""
        obj = City()
        self.assertEqual(type(obj.id), str)

    def test_created_type(self):
        """Verify that the 'created_at' attribute is of type datetime."""
        obj = City()
        self.assertEqual(type(obj.created_at), datetime)

    def test_updated_type(self):
        """Verify that the 'updated_at' attribute is of type datetime."""
        obj = City()
        self.assertEqual(type(obj.updated_at), datetime)

    def test_different_id(self):
        """Verify that two instances have different 'id' values."""
        x = City()
        y = City()
        self.assertNotEqual(x.id, y.id)

    def test_public_attribute(self):
        """Test case to check if setting a public attribute works"""
        instance = City()
        instance.name = "San Francisco"
        self.assertEqual(instance.name, "San Francisco")

    def test_update_at(self):
        """Verify that 'updated_at' changes after updating
        an attribute and saving."""
        x = City()
        sleep(1)
        x.name = "Updated City"
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_update_attributes(self):
        """Verify that attributes can be updated and saved."""
        kwargs = {
            'name': 'Los Angeles',
        }

        obj = City(**kwargs)
        self.assertEqual(obj.name, "Los Angeles")
        obj.name = "San Diego"
        self.assertEqual(obj.name, "San Diego")

    def test_created_different_time(self):
        """Verify that 'created_at' times are different for
            two instances created with a time gap.
        """
        x = City()
        sleep(1)
        y = City()
        self.assertNotEqual(x.created_at, y.created_at)

    def test_updated_different_time(self):
        """Verify that 'updated_at' times are different after saving
         two instances with different changes.
         """
        x = City()
        y = City()
        x.name = "Chicago"
        x.save()
        y.name = "New York"
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

        instance = City(**kwargs)

        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_field, 'custom_value')
        self.assertEqual(instance.created_at,
                         datetime.fromisoformat('2024-02-11T12:34:56'))
        self.assertEqual(instance.updated_at,
                         datetime.fromisoformat('2024-02-11T12:45:00'))

    def test_create_with_kwargs_type(self):
        """Test creating a new instance"""
        kwargs = {
            'name': 'Seattle',
        }
        obj = City(**kwargs)
        self.assertEqual(type(obj.name), str)

    def test_kwargs_values(self):
        """Test kwargs values"""
        kwargs = {
            'name': 'Seattle',
        }
        obj = City(**kwargs)
        self.assertEqual(obj.name, 'Seattle')


if __name__ == "__main__":
    unittest.main()
