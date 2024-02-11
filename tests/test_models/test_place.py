#!/usr/bin/python3
""" Defines unittests for models/place.py. """

import unittest
from time import sleep
from datetime import datetime
from models.place import Place


class TestPlace_obj_init(unittest.TestCase):
    def test_obj_type(self):
        """Verify that the object is an instance of Place."""
        obj = Place()
        self.assertEqual(type(obj), Place)

    def test_multiple_instances(self):
        """Test handling multiple instances."""
        place1 = Place()
        place2 = Place()

        self.assertNotEqual(place1.id, place2.id)
        place1.name = "Place1"
        place2.name = "Place2"

        self.assertEqual(place1.name, "Place1")
        self.assertEqual(place2.name, "Place2")

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

        instance = Place(**kwargs)
        self.assertNotIn('__class__', instance.__dict__)

    def test_id_type(self):
        """Verify that the 'id' attribute is of type str."""
        obj = Place()
        self.assertEqual(type(obj.id), str)

    def test_created_type(self):
        """Verify that the 'created_at' attribute is of type datetime."""
        obj = Place()
        self.assertEqual(type(obj.created_at), datetime)

    def test_updated_type(self):
        """Verify that the 'updated_at' attribute is of type datetime."""
        obj = Place()
        self.assertEqual(type(obj.updated_at), datetime)

    def test_different_id(self):
        """Verify that two instances have different 'id' values."""
        x = Place()
        y = Place()
        self.assertNotEqual(x.id, y.id)

    def test_public_attribute(self):
        """Test case to check if setting a public attribute works"""
        instance = Place()
        instance.name = "Beautiful Place"
        self.assertEqual(instance.name, "Beautiful Place")

    def test_update_at(self):
        """Verify that 'updated_at' changes after updating an
        attribute and saving."""
        x = Place()
        sleep(1)
        x.name = "Updated Place"
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_update_attributes(self):
        """Verify that attributes can be updated and saved."""
        kwargs = {
            'name': 'Cozy Cabin',
            'price_by_night': 150,
        }

        obj = Place(**kwargs)
        self.assertEqual(obj.name, "Cozy Cabin")
        obj.name = "Luxury Villa"
        self.assertEqual(obj.name, "Luxury Villa")

    def test_created_different_time(self):
        """Verify that 'created_at' times are different for
            two instances created with a time gap.
        """
        x = Place()
        sleep(1)
        y = Place()
        self.assertNotEqual(x.created_at, y.created_at)

    def test_updated_different_time(self):
        """Verify that 'updated_at' times are different after saving
         two instances with different changes.
         """
        x = Place()
        y = Place()
        x.name = "Seaside Retreat"
        x.save()
        y.name = "Mountain Getaway"
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

        instance = Place(**kwargs)

        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_field, 'custom_value')
        self.assertEqual(instance.created_at,
                         datetime.fromisoformat('2024-02-11T12:34:56'))
        self.assertEqual(instance.updated_at,
                         datetime.fromisoformat('2024-02-11T12:45:00'))

    def test_create_with_kwargs_type(self):
        """Test creating a new instance"""
        kwargs = {
            'name': 'Rustic Cottage',
            'price_by_night': 120,
        }
        obj = Place(**kwargs)
        self.assertEqual(type(obj.price_by_night), int)
        self.assertEqual(type(obj.name), str)

    def test_kwargs_values(self):
        """Test kwargs values"""
        kwargs = {
            'name': 'Oceanfront Paradise',
            'price_by_night': 200,
        }
        obj = Place(**kwargs)
        self.assertEqual(obj.name, 'Oceanfront Paradise')
        self.assertEqual(obj.price_by_night, 200)


class TestPlaceAttributes(unittest.TestCase):
    def test_default_attribute_values(self):
        """Test that default attribute values are as expected."""
        place = Place()
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

    def test_attribute_types(self):
        """Test that attribute types are as expected."""
        place = Place()
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_attribute_assignment(self):
        """Test assigning values to attributes."""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Cozy Place"
        place.description = "A cozy and comfortable place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Cozy Place")
        self.assertEqual(place.description,
                         "A cozy and comfortable place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_attribute_assignment_type(self):
        """Test assigning values of correct types to attributes."""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Cozy Place"
        place.description = "A cozy and comfortable place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_to_dict_with_attributes(self):
        """Test to_dict method with custom attributes."""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Cozy Place"
        place.description = "A cozy and comfortable place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["amenity1", "amenity2"]

        expected_dict = {
            'id': place.id,
            'created_at': place.created_at.isoformat(),
            'updated_at': place.updated_at.isoformat(),
            'city_id': 'city123',
            'user_id': 'user123',
            'name': 'Cozy Place',
            'description': 'A cozy and comfortable place',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['amenity1', 'amenity2'],
            '__class__': 'Place'
        }

        self.assertEqual(place.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
