#!/usr/bin/python3

"""
    This is a test that tests all the functions in the console.py file, by providing 
    inputs and expected outputs that will be returned by the program
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ create an object of the command line interpreter from class HBNBCommand """
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new=StringIO())
    def test_create(self):
        """ Test the create command used to create new objects """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertIn("BaseModel", f.getvalue().strip())

    @patch('sys.stdout', new=StringIO())
    def test_show(self):
        """ Test the show command for displaying the entries of file storage object """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new=StringIO())
    def test_destroy(self):
        """ Test the deletion command to delete a certain entry in the file storage object """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new=StringIO())
    def test_all(self):
        """ Test the all command that is used to print all the entries in the file storage object """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertEqual(f.getvalue().strip(), "[]")

    @patch('sys.stdout', new=StringIO())
    def test_update(self):
        """ Test the update command used to update a record or records to the file storage object """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234 attribute value")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new=StringIO())
    def test_quit(self):
        """ Test the quit command for exiting the command line interpreter """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    @patch('sys.stdout', new=StringIO())
    def test_EOF(self):
        """ Test the EOF (End Of File) command for specifying the end of file, led to exit of the command line """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    @patch('sys.stdout', new=StringIO())
    def test_invalid_command(self):
        """ Tests for invalid command - a command that was never defined as a function in the HBNBCommand class """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            self.assertIn("invalid syntax", f.getvalue().strip().lower())


if __name__ == "__main__":
    unittest.main()