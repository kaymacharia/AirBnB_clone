#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsoleHelp(unittest.TestCase):
    """
    Test class for console
    """

    def setUp(self):
        """sets up the console class before every test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """passes"""
        pass

    def test_help_quit_command(self):
        with patch ('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_help_EOF_command(self):
        with patch ('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

    def test_help_emptyline_command(self):
        with patch ('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
