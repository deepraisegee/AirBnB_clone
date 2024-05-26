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
            HBNBCommand().onecmd("quit")
            HBNBCommand().onecmd("EOF")
            HBNBCommand().onecmd("help")
            HBNBCommand().onecmd("empty line")

    def test_all_crud_commands(self):
        """test for all CRUD commands on the standard output"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("show BaseModel")
            HBNBCommand().onecmd("destroy BaseModel")
            HBNBCommand().onecmd("all BaseModel")
            HBNBCommand().onecmd("update BaseModel")

    def test_orm_command_for_base_model_class(self):
        """test for ORM commands for BaseModel class"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            HBNBCommand().onecmd("BaseModel.count()")
            HBNBCommand().onecmd('BaseModel.show("id")')
            HBNBCommand().onecmd('BaseModel.destroy("id")')
            HBNBCommand().onecmd(
                'BaseModel.update("id", "attribute_name", "string_value")'
            )
            HBNBCommand().onecmd(
                'BaseModel.update("id", { "attribute_name": "string_value" })'
            )

    def test_orm_command_for_user_class(self):
        """test for ORM commands for User class"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            HBNBCommand().onecmd("User.count()")
            HBNBCommand().onecmd('User.show("id")')
            HBNBCommand().onecmd('User.destroy("id")')
            HBNBCommand().onecmd(
                'User.update("id", "attribute_name", "string_value")'
            )
            HBNBCommand().onecmd(
                'User.update("id", { "attribute_name": "string_value" })'
            )

    def test_orm_command_for_city_class(self):
        """test for ORM commands for City class"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            HBNBCommand().onecmd("City.count()")
            HBNBCommand().onecmd('City.show("id")')
            HBNBCommand().onecmd('City.destroy("id")')
            HBNBCommand().onecmd(
                'City.update("id", "attribute_name", "string_value")'
            )
            HBNBCommand().onecmd(
                'City.update("id", { "attribute_name": "string_value" })'
            )

    def test_orm_command_for_state_class(self):
        """test for ORM commands for State class"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            HBNBCommand().onecmd("State.count()")
            HBNBCommand().onecmd('State.show("id")')
            HBNBCommand().onecmd('State.destroy("id")')
            HBNBCommand().onecmd(
                'State.update("id", "attribute_name", "string_value")'
            )
            HBNBCommand().onecmd(
                'State.update("id", { "attribute_name": "string_value" })'
            )

    def test_orm_command_for_place_class(self):
        """test for ORM commands for Place class"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            HBNBCommand().onecmd("Place.count()")
            HBNBCommand().onecmd('Place.show("id")')
            HBNBCommand().onecmd('Place.destroy("id")')
            HBNBCommand().onecmd(
                'Place.update("id", "attribute_name", "string_value")'
            )
            HBNBCommand().onecmd(
                'Place.update("id", { "attribute_name": "string_value" })'
            )

    def test_orm_command_for_amenity_class(self):
        """test for ORM commands for Amenity class"""
        with patch("sys.stdout", new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            HBNBCommand().onecmd("Amenity.count()")
            HBNBCommand().onecmd('Amenity.show("id")')
            HBNBCommand().onecmd('Amenity.destroy("id")')
            HBNBCommand().onecmd(
                'Amenity.update("id", "attribute_name", "string_value")'
            )
            HBNBCommand().onecmd(
                'Amenity.update("id", { "attribute_name": "string_value" })'
            )
