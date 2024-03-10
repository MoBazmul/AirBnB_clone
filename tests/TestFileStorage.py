#!/usr/bin/python3

"""
    This is a test file that test the functions in file_storage.py by providing
    the inputs and expected outputs; assert the results or output of the functions
    based on the inputs provided
"""

import unittest
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ Initialize storage """
        self.storage = FileStorage()

    def tearDown(self):
        """ Delete the file path to the file storage """
        if os.path.exists(self.storage.__file_path):
            os.remove(self.storage.__file_path)

    def test_save_and_reload(self):
        """ Testing the save() method and reload method by providing inputs and expected outputs """
        state = State(name='Kenya')
        city = City(name='Mombasa', state_id=state.uid)
        amenity = Amenity(name='Wifi')
        place = Place(name='Comfortable Apartment', city_id=city.uid, user_id='baz23')
        review = Review(place_id=place.uid, user_id='baz23', text='Beautiful Place, Amazing!')

        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(place)
        self.storage.new(review)
        
        self.storage.save()

        storage._FileStorage__objects = {}

        self.storage.reload()

        self.assertEqual(len(self.storage.all()), 5)
        self.assertTrue(f"State.{state.uid}" in self.storage.all())
        self.assertTrue(f"City.{city.uid}" in self.storage.all())
        self.assertTrue(f"Amenity.{amenity.uid}" in self.storage.all())
        self.assertTrue(f"Place.{place.uid}" in self.storage.all())
        self.assertTrue(f"Review.{review.uid}" in self.storage.all())

        # Check attributes of reloaded objects
        reloaded_state = self.storage.all()[f"State.{state.uid}"]
        self.assertEqual(reloaded_state.name, 'Kenya')
        reloaded_city = self.storage.all()[f"City.{city.uid}"]
        self.assertEqual(reloaded_city.name, 'Mombasa')
        self.assertEqual(reloaded_city.state_id, state.uid)
        reloaded_amenity = self.storage.all()[f"Amenity.{amenity.uid}"]
        self.assertEqual(reloaded_amenity.name, 'Wifi')
        reloaded_place = self.storage.all()[f"Place.{place.uid}"]
        self.assertEqual(reloaded_place.name, 'Comfortable Apartment')
        self.assertEqual(reloaded_place.city_id, city.uid)
        self.assertEqual(reloaded_place.user_id, 'baz23')
        reloaded_review = self.storage.all()[f"Review.{review.uid}"]
        self.assertEqual(reloaded_review.place_id, place.uid)
        self.assertEqual(reloaded_review.user_id, 'baz23')
        self.assertEqual(reloaded_review.text, 'Beautiful Place, Amazing!')

if __name__ == '__main__':
    unittest.main()