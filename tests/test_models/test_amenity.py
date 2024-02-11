#!/usr/bin/python3
""" Defines unittests for models/amenity.py. """
from time import sleep
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenityInitialization(unittest.TestCase):
    def test_obj_type(self):
        """Verify that the object is an instance of Amenity."""
        obj = Amenity()
        self.assertEqual(type(obj), Amenity)

    def test_multiple_instances(self):
        """Test handling multiple instances."""
        amenity1 = Amenity()
        amenity2 = Amenity()

        self.assertNotEqual(amenity1.id, amenity2.id)
        amenity1.name = "Amenity1"
        amenity2.name = "Amenity2"

        self.assertEqual(amenity1.name, "Amenity1")
        self.assertEqual(amenity2.name, "Amenity2")

    def test_no_class_attribute(self):
        """Test if __class__ attribute is not set in the __init__ method."""
        kwargs = {
            'id': 'test_id',
            'created_at': '2024-02-11T12:34:56',
            'updated_at': '2024-02-11T12:45:00',
            'custom_field': 'custom_value',
            '__class__': 'ShouldNotBeSet'
        }

        instance = Amenity(**kwargs)
        self.assertNotIn('__class__', instance.__dict__)

    def test_id_type(self):
        """Verify that the 'id' attribute is of type str."""
        obj = Amenity()
        self.assertEqual(type(obj.id), str)

    def test_created_type(self):
        """Verify that the 'created_at' attribute is of type datetime."""
        obj = Amenity()
        self.assertEqual(type(obj.created_at), datetime)

    def test_updated_type(self):
        """Verify that the 'updated_at' attribute is of type datetime."""
        obj = Amenity()
        self.assertEqual(type(obj.updated_at), datetime)

    def test_different_id(self):
        """Verify that two instances have different 'id' values."""
        x = Amenity()
        y = Amenity()
        self.assertNotEqual(x.id, y.id)

    def test_public_attribute(self):
        """Test case to check if setting a public attribute works"""
        instance = Amenity()
        instance.name = "Swimming Pool"
        self.assertEqual(instance.name, "Swimming Pool")

    def test_update_at(self):
        """Verify that 'updated_at' changes after updating an
        attribute and saving."""
        x = Amenity()
        sleep(1)
        x.name = "Updated Amenity"
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_update_attributes(self):
        """Verify that attributes can be updated and saved."""
        kwargs = {
            'name': 'Gym',
        }

        obj = Amenity(**kwargs)
        self.assertEqual(obj.name, "Gym")
        obj.name = "Sauna"
        self.assertEqual(obj.name, "Sauna")

    def test_created_different_time(self):
        """Verify that 'created_at' times are different for
            two instances created with a time gap.
        """
        x = Amenity()
        sleep(1)
        y = Amenity()
        self.assertNotEqual(x.created_at, y.created_at)

    def test_updated_different_time(self):
        """Verify that 'updated_at' times are different after saving
         two instances with different changes.
         """
        x = Amenity()
        sleep(1)
        y = Amenity()
        x.name = "Outdoor Terrace"
        x.save()
        y.name = "Rooftop Lounge"
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

        instance = Amenity(**kwargs)

        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_field, 'custom_value')
        self.assertEqual(instance.created_at,
                         datetime.fromisoformat('2024-02-11T12:34:56'))
        self.assertEqual(instance.updated_at,
                         datetime.fromisoformat('2024-02-11T12:45:00'))

    def test_create_with_kwargs_type(self):
        """Test creating a new instance"""
        kwargs = {
            'name': 'Outdoor Pool',
        }
        obj = Amenity(**kwargs)
        self.assertEqual(type(obj.name), str)

    def test_kwargs_values(self):
        """Test kwargs values"""
        kwargs = {
            'name': 'Fitness Center',
        }
        obj = Amenity(**kwargs)
        self.assertEqual(obj.name, 'Fitness Center')


if __name__ == "__main__":
    unittest.main()
