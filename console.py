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


class Console(cmd.Cmd):
    """The processor class for all the commads"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """end of file"""
        return True

    def do_quit(self, line):
        """exit out of the program"""
        sys.exit(0)


if __name__ == "__main__":
    Console().cmdloop()
