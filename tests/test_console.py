#!/usr/bin/python3

"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import unittest
from io import StringIO
from unittest.mock import patch
import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """
    
    def setUp(self):
        """Redirecting stdin and stdout"""
        self.console = HBNBCommand()
    
    def tearDown(self):
        """ Restart the program, running like a newly created program
        with no preexisting files """
        pass
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """ Test the Quit function used to exit the cmd line interpreter """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """ Test for the End Of File function """
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """ Test for the empty line function """
        self.console.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), '')
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """
        Redirects stdin and stdout to the mock module
        """
        self.console.onecmd("create BaseModel")
        self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """ Test if the show function works """
        self.console.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """ Test if the destroy function works """
        self.console.onecmd("destroy BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """ Test for the all function that is used to display all object's information """
        self.console.onecmd("all BaseModel")
        self.assertIn("[]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """ Test the update function used to update newly created or deleted objects to the file storage """
        self.console.onecmd("update BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """ Test the count method used to count how many objects that have been created in the cmd line interpreter """
        self.console.onecmd("count BaseModel")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    def test_default(self):
        """ Test for the default method for default behavior if the object is not passed as cmd line argument """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("MyModel.show()")
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

if __name__ == '__main__':
    """ Run the test """
    unittest.main()

