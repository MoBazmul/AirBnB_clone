import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
    
    def tearDown(self):
        pass
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.console.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), '')
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        self.console.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        self.console.onecmd("destroy BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.console.onecmd("all BaseModel")
        self.assertIn("[]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        self.console.onecmd("update BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        self.console.onecmd("count BaseModel")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    def test_default(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("MyModel.show()")
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

