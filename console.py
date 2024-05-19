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


class HBNBCommand(cmd.Cmd):
    """The processor class for all the commads"""

    prompt = "(hbnb) "

    def emptyline(self):
        """do nothing when the line is empty"""
        pass

    def do_EOF(self, line):
        """end of file"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit(0)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
