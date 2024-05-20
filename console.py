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

    def do_create(self, arg):
        """
        Create new instance of a model.
        Usage:
            create <ModelName>
        """
        if not arg.strip():
            print("** class name missing **")
            return
        if arg not in models.CLASSES:
            print("** class doesn't exist **")
            return
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
        args = arg.split(" ")
        if not arg.strip():
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2 and args[0] not in models.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            try:
                class_name = args[0]
                obj_id = f"{class_name}.{args[1]}"
                print(models.storage.all()[obj_id])
            except KeyError:
                print("** no instance found **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
