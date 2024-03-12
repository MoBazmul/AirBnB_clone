import unittest
from unittest.mock import patch
from io import StringIO
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, '')
        self.assertEqual(mock_stdout.getvalue(), '')

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(mock_stdout.getvalue(), '')

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertEqual(mock_stdout.getvalue(), '')

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, '')
        self.assertEqual(mock_stdout.getvalue(), '')

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    @patch('sys.stdout', new_callable=StringIO)
    def test_attributes(self, mock_stdout):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')
        self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()

