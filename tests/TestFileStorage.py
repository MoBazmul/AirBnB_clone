#!/usr/bin/python3

"""
    This is a test file that test the functions in file_storage.py by providing
    the inputs and expected outputs; assert the results or output of the functions
    based on the inputs provided
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

import unittest
import json
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """ Tests for the functionality of the FileStorage class """
    def setUp(self):
        """ Initialize the storage object for the test cases """
        from models import storage
        return storage

    def tearDown(self):
        """ Destroy the object file storage to empty file storage - with no data in it """
        from models import storage
        try:
            with open(storage, 'w') as f:
                f.write(json.dumps({}))
        except Exception as e:
            print(e)

    @patch('sys.stdout', new_callable=StringIO)
    def test_new(self, mock_stdout):
        """ Test the creation of new base class """
        from models import storage
        storage.new(BaseModel())
        self.assertTrue(len(storage.all()) == 1)
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_save(self, mock_stdout):
        """ Test the save method that save object to the file storage """
        from models import storage
        storage.new(BaseModel())
        storage.save()
        with open(storage, 'r') as f:
            data = json.load(f)
            self.assertTrue(len(data) == 1)
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_reload(self, mock_stdout):
        """ Test the reload method """
        from models import storage
        storage.new(BaseModel())
        storage.save()
        storage.reload()
        self.assertTrue(len(storage.all()) == 1)
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_reload_exception(self, mock_stdout):
        """ Tets the reload exception of the reload method """
        from models import storage
        # Remove file to trigger FileNotFoundError
        try:
            with open(storage, 'w') as f:
                f.write('')
        except Exception as e:
            print(e)
        
        with self.assertRaises(FileNotFoundError):
            storage.reload()
        self.assertIn("FileNotFoundError", mock_stdout.getvalue())

if __name__ == '__main__':
    """ Run the tests """
    unittest.main()

