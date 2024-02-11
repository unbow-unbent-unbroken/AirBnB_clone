#!/usr/bin/python3
"""Review Unittest files"""

from time import sleep
import unittest
from datetime import datetime
from models.review import Review


class TestReviewInitialization(unittest.TestCase):
    def test_obj_type(self):
        """Verify that the object is an instance of Review."""
        obj = Review()
        self.assertEqual(type(obj), Review)

    def test_multiple_instances(self):
        """Test handling multiple instances."""
        review1 = Review()
        review2 = Review()

        self.assertNotEqual(review1.id, review2.id)
        review1.text = "Review1"
        review2.text = "Review2"

        self.assertEqual(review1.text, "Review1")
        self.assertEqual(review2.text, "Review2")

    def test_no_class_attribute(self):
        """Test if __class__ attribute is not set in the __init__ method."""
        kwargs = {
            'id': 'test_id',
            'created_at': '2024-02-11T12:34:56',
            'updated_at': '2024-02-11T12:45:00',
            'custom_field': 'custom_value',
            '__class__': 'ShouldNotBeSet'
        }

        instance = Review(**kwargs)
        self.assertNotIn('__class__', instance.__dict__)

    def test_id_type(self):
        """Verify that the 'id' attribute is of type str."""
        obj = Review()
        self.assertEqual(type(obj.id), str)

    def test_created_type(self):
        """Verify that the 'created_at' attribute is of type datetime."""
        obj = Review()
        self.assertEqual(type(obj.created_at), datetime)

    def test_updated_type(self):
        """Verify that the 'updated_at' attribute is of type datetime."""
        obj = Review()
        self.assertEqual(type(obj.updated_at), datetime)

    def test_different_id(self):
        """Verify that two instances have different 'id' values."""
        x = Review()
        y = Review()
        self.assertNotEqual(x.id, y.id)

    def test_public_attribute(self):
        """Test case to check if setting a public attribute works"""
        instance = Review()
        instance.text = "Good review"
        self.assertEqual(instance.text, "Good review")

    def test_update_at(self):
        """Verify that 'updated_at' changes after
         an attribute and saving."""
        x = Review()
        sleep(1)
        x.text = "Updated review"
        x.save()
        self.assertNotEqual(x.created_at, x.updated_at)

    def test_update_attributes(self):
        """Verify that attributes can be updated and saved."""
        kwargs = {
            'text': 'Original review',
            'rating': 5,
        }

        obj = Review(**kwargs)
        self.assertEqual(obj.text, "Original review")
        obj.text = "Modified review"
        self.assertEqual(obj.text, "Modified review")

    def test_created_different_time(self):
        """Verify that 'created_at' times are different for
            two instances created with a time gap.
        """
        x = Review()
        sleep(1)
        y = Review()
        self.assertNotEqual(x.created_at, y.created_at)

    def test_updated_different_time(self):
        """Verify that 'updated_at' times are different after saving
         two instances with different changes.
         """
        x = Review()
        y = Review()
        x.text = "First review"
        x.save()
        y.text = "Second review"
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

        instance = Review(**kwargs)

        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.custom_field, 'custom_value')
        self.assertEqual(instance.created_at,
                         datetime.fromisoformat('2024-02-11T12:34:56'))
        self.assertEqual(instance.updated_at,
                         datetime.fromisoformat('2024-02-11T12:45:00'))

    def test_create_with_kwargs_type(self):
        """Test creating a new instance"""
        kwargs = {
            'text': 'Detailed review',
            'rating': 4,
        }
        obj = Review(**kwargs)
        self.assertEqual(type(obj.rating), int)
        self.assertEqual(type(obj.text), str)

    def test_kwargs_values(self):
        """Test kwargs values"""
        kwargs = {
            'text': 'In-depth review',
            'rating': 5,
        }
        obj = Review(**kwargs)
        self.assertEqual(obj.text, 'In-depth review')
        self.assertEqual(obj.rating, 5)


if __name__ == "__main__":
    unittest.main()
