#!/usr/bin/python3

"""
    This is a test file that test the functions in base_model.py by providing
    the inputs and expected outputs; assert the results or output of the functions
    based on the inputs provided
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """ Create an instance of the BaseModel class """
        self.base = BaseModel(name='Mohammed', age=25)

    def tearDown(self):
        """ Initialize the file storage to empty dictionary """
        storage.__file_path = {}

    def test_save(self):
        """ Test the save function, checks if the save function can correctly save to the file storage """
        with patch('sys.stdout', new=StringIO()) as file:
            self.base.save()
            self.assertTrue(isinstance(self.base.created_at, str))
            self.assertTrue(isinstance(self.base.updated_at, str))
            self.assertEqual(file.getvalue(), '')

    def test_to_dict(self):
        """ Test the change from class object to a dictionary object """
        with patch('sys.stdout', new=StringIO()) as file:
            self.base.save()
            obj_dict = self.base.to_dict()
            self.assertEqual(obj_dict['__class__'], 'BaseModel')
            self.assertEqual(obj_dict['name'], 'Mohammed')
            self.assertEqual(obj_dict['age'], 25)
            self.assertTrue(isinstance(obj_dict['created_at'], str))
            self.assertTrue(isinstance(obj_dict['updated_at'], str))
            self.assertEqual(file.getvalue(), '')

    def test_str(self):
        """ Test the printed output of our program """
        expected_output = """
            [<BaseModel>]
            (<class 'str'>)
            <{'name': 'Mohammed', 'age': 25, 'uid': '12234', 'created_at': '02/12/202408:32:23.47663', 'updated_at': '14/12/202410:12:53.32663'}>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.base.uid = '12234'
            self.base.created_at = '02/12/202408:32:23.47663'
            self.base.updated_at = '14/12/202410:12:53.32663'
            print(self.base)
            self.assertEqual(f.getvalue().strip(), expected_output.strip())
            
            
if __name__ == '__main__':
    """ Run the tests """
    unittest.main()
            
