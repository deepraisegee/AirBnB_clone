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

    def default(self, line):
        """Handle unrecognized command"""
        commands = [i.strip() for i in line.split(".")]
        if len(commands) != 2:
            return super().default(line)
        if commands[0] not in models.CLASSES:
            return super().default(line)
        if commands[1] == "all()":
            self.do_all(commands[0])
            return
        if commands[1] == "count()":
            print(len(models.storage.filter(commands[0])))
            return
        if "show" in commands[1]:
            # validate if id was passed
            if len(commands[1][4:]) < 5:
                # length of id will surely greater than 5
                print("** instance id missing **")
                return

            # slice out the instance id
            try:
                obj_id = commands[1][6:-2]
                self.do_show(" ".join([commands[0], obj_id]))
                return
            except IndexError:
                return
        if "destroy" in commands[1]:
            # validate if id was passed
            if len(commands[1][7:]) < 5:
                # length of id will surely greater than 5
                print("** instance id missing **")
                return

            # slice out the instance id
            try:
                obj_id = commands[1][9:-2]
                self.do_destroy(" ".join([commands[0], obj_id]))
                return
            except IndexError:
                return
        if "update" in commands[1]:
            # validate if id was passed
            if len(commands[1][6:]) < 5:
                # length of id will surely greater than 5
                print("** instance id missing **")
                return

            # slice out the instance id
            params = [i.strip() for i in commands[1].split(", ")]
            class_name = commands[0]
            # let's do some validation here
            if params:
                p = params
                _id = p[0][8:-2] if len(p) == 1 else p[0][8:-1]
                obj_id = f"{commands[0]}.{_id}"
                try:
                    models.storage.all()[obj_id]
                except KeyError:
                    print("Error")
                    print("** no instance found **")
                    return
            if len(params[0].split("(")) < 2:
                print("** instance id missing **")
                return
            if len(params) == 1:
                print("** attribute name missing **")
                return
            if len(params) > 1 and params[1].startswith("{"):
                try:
                    # parse the second argument to python dictionary
                    opt = commands[1]
                    data = opt[opt.index("{"):opt.index("}") + 1]
                    models.storage.update(obj_id, data)
                    return
                except IndexError:
                    return
            if len(params) == 2:
                print("** value missing **")
                return
            try:
                p = params
                attr = p[1][1:-1]
                val = p[2][1:-2] if '"' in p[2] or "'" in p[2] else p[2][:-1]
                self.do_update(" ".join([class_name, _id, attr, val]))
                return
            except IndexError:
                return

        return super().default(line)

    def do_EOF(self, arg):
        """Handle end of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        sys.exit(0)

    @staticmethod
    def validate_class_name(arg):
        """A static method to validate only class name"""
        if arg and arg.split(" ")[0] not in models.CLASSES:
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
            all <ModelName>
        """
        if not HBNBCommand.validate_class_name(arg):
            return
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
        if not arg:
            print("** class name missing **")
            return
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
            update <ModelName> <instance_id> <attribute_name> <attribute_value>
        """
        args = arg.split(" ")
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj_id = HBNBCommand.validate_args(arg)
        if not obj_id:
            return
        attr, val = args[2], args[3]
        models.storage.update(obj_id, attr=attr, val=val)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage:
            destroy <ModelName> <instance_id>
        """
        obj_id = HBNBCommand.validate_args(arg)
        if obj_id is not None:
            models.storage.delete(obj_id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
