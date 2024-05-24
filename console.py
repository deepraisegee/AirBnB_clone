#!/usr/bin/python3

"""
This module is an entrypoint for the app.

Usage:
    By running this module, the (hbnb) prompt loop
    showup and ready to accept command to interact
    with the AirBnB app.
"""
import cmd
import sys

import models
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The processor class for all the commads"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Handle when the line is empty"""
        pass

    def do_EOF(self, arg):
        """Handle end of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        sys.exit(0)

    @staticmethod
    def validate_class_name(arg):
        """A static method to validate only class name"""
        if arg not in models.CLASSES:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def validate_args(arg):
        """A static method for validating input arguments"""
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in models.CLASSES:
            print("** class doesn't exist **")
            return
        obj_id = f"{args[0]}.{args[1]}"
        try:
            models.storage.all()[obj_id]
        except KeyError:
            print("** no instance found **")
        else:
            return obj_id

    def do_all(self, arg):
        """
        List all instances based or not on the class name.
        Usage:
            all <ClassName>
        """
        if arg:
            print(models.storage.filter(class_name=arg))
            return
        print(models.storage.filter())

    def do_create(self, arg):
        """
        Create new instance of a model.
        Usage:
            create <ModelName>
        """
        if HBNBCommand.validate_class_name(arg):
            obj = models.CLASSES[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        Usage:
            show <ModelName> <instance_id>
        """
        obj_id = HBNBCommand.validate_args(arg)
        if obj_id is not None:
            print(models.storage.get(obj_id))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        Usage:
            update <ClassName> <instance_id> <attribute_name> <attribute_value>
        """
        obj_id = HBNBCommand.validate_args(arg)
        if not obj_id:
            return
        args = arg.split(" ")
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr, val = args[2], args[3]
        models.storage.update(obj_id, attr, val)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage:
            destroy <ClassName> <instance_id>
        """
        obj_id = HBNBCommand.validate_args(arg)
        if obj_id is not None:
            models.storage.delete(obj_id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
