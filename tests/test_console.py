#!/usr/bin/python3
"""
Main module console test cases
"""
import io
import unittest
from unittest.mock import patch

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test class for all the console commands"""

    def test_all_command(self):
        """test for `help` command on standard output"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("all")
