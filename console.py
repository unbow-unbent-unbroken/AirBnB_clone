#!/usr/bin/python3
"""Console module"""
import re
import cmd
import models
import shlex
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def my_strip(args):
    """creates tokens"""
    modified_text = args.replace('(', '.').replace(')',
                                                   '').replace('"', '')
    return modified_text.split('.')


def get_numeric_value(s):
    """change string to numeric"""
    try:
        return int(s) if s.isdigit() else float(s)
    except ValueError:
        return


def is_numeric(s):
    """check if string is numeric"""
    try:
        float_value = float(s)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    """
       HBNBCommand class
    """
    prompt = '(hbnb) '
    __cnames = [
        "BaseModel", "User",
        "State", "City", "Amenity",
        "Place", "Review"]

    def default(self, line):
        """executed when unrecognized line"""
        args = line.split('.')
        if len(args) == 2 and args[1] == "all()":
            self.do_all(args[0])
        elif len(args) == 2 and args[1] == "count()":
            x = len([k for k in models.storage.all().keys()
                     if k.split('.')[0] == args[0]])
            print(x)
        elif len(args) > 1:
            new_args = my_strip(line)
            if new_args[1] == "show":
                self.do_show(new_args[0] + " " + new_args[2])
            elif new_args[1] == "destroy":
                self.do_destroy(new_args[0] + " " + new_args[2])
            elif new_args[1] == "update":
                p = re.compile(r'(\w+)\.update\("(.*?)", "(.*?)", (.*)\)')
                match = p.match(line)
                if match:
                    c_name, instance_id, attr_name, attr_value = match.groups()
                    self.do_update(f"{c_name} {instance_id} "
                                   f"{attr_name} {attr_value}")

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create a new object"""
        if not line:
            print("** class name missing **")
        elif line not in self.__cnames:
            print("** class doesn't exist **")
        else:
            obj = eval(line)()
            models.storage.save()
            print(obj.id)

    def do_show(self, line):
        """Show the given object"""
        result = shlex.split(line)
        if not result:
            print("** class name missing **")
        elif result[0] not in self.__cnames:
            print("** class doesn't exist **")
        elif len(result) == 1:
            print("** instance id missing **")
        elif f"{result[0]}.{result[1]}" not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[f"{result[0]}.{result[1]}"])

    def do_destroy(self, line):
        """Destroy the given object"""
        result = line.split()
        if not result:
            print("** class name missing **")
        elif result[0] not in self.__cnames:
            print("** class doesn't exist **")
        elif len(result) == 1:
            print("** instance id missing **")
        elif f"{result[0]}.{result[1]}" not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()[f"{result[0]}.{result[1]}"]
            models.storage.save()

    def do_all(self, line):
        """Returns all instances """
        result_list = []
        if line not in self.__cnames and line:
            print("** class doesn't exist **")
            return
        elif line:
            for k, obj in models.storage.all().items():
                if line == k.split('.')[0]:
                    result_list.append(str(obj))
        else:
            for k, obj in models.storage.all().items():
                result_list.append(str(obj))
        print(result_list)

    def do_update(self, line):
        """update the object attributes"""
        result = line.split()
        if not result:
            print("** class name missing **")
        elif result[0] not in self.__cnames:
            print("** class doesn't exist **")
        elif len(result) == 1:
            print("** instance id missing **")
        elif (len(result) > 1 and f"{result[0]}.{result[1]}"
              not in models.storage.all()):
            print("** no instance found **")
        elif len(result) == 2:
            print("** attribute name missing **")
        elif len(result) == 3:
            print("** value missing **")
        else:
            obj = models.storage.all()[f"{result[0]}.{result[1]}"]
            if is_numeric(result[3]):
                new_value = get_numeric_value(result[3])
                setattr(obj, result[2], new_value)
            else:
                setattr(obj, result[2], result[3])
            models.storage.all()[f"{result[0]}.{result[1]}"] = obj
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
