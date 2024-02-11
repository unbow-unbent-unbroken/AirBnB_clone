#!/usr/bin/python3
""" Defines unittests for models/enfine/file_storage.py. """
import unittest
import json
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all() method of FileStorage."""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new() method of FileStorage."""
        bm = BaseModel()
        self.storage.new(bm)
        self.assertIn("BaseModel.{}".format(bm.id), self.storage.all())

    def test_save_reload(self):
        """Test the save() and reload() methods of FileStorage."""
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.storage.new(bm1)
        self.storage.new(bm2)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn("BaseModel.{}".format(bm1.id), new_storage.all())
        self.assertIn("BaseModel.{}".format(bm2.id), new_storage.all())

    def test_save_file_exists(self):
        """Test save() method when the file already exists."""
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.storage.new(bm1)
        self.storage.new(bm2)
        self.storage.save()

        bm3 = BaseModel()
        self.storage.new(bm3)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn("BaseModel.{}".format(bm1.id), new_storage.all())
        self.assertIn("BaseModel.{}".format(bm2.id), new_storage.all())
        self.assertIn("BaseModel.{}".format(bm3.id), new_storage.all())


if __name__ == "__main__":
    unittest.main()
