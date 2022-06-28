#!/usr/bin/python3
"""Defines the console."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Defines the Holberton command interpreter"""

prompt = "(hbnb) "
__classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        }
def emptyline(self):
    """Do nothing receiving an empty line"""
    pass

def do_quit(self, arg):
    """Exit the program"""
    return True

def do_EOF(self, arg):
    """EOF signal to exit the program"""
    print("")
    return True

def do_create(self, arg):
    """Create a new class instance and print its id"""
    argl = parse(arg)
    if len(argl) == 0:
        print("** class name missing **")
    elif argl[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    else:
        print(eval(argl[0])().id)
        storage.save()

def do_show(self, arg):
    """Display the string representation of a class instance of a given id
    """
    argl = parse(arg)
    objdict = storage.all()
    if len(argl) == 0:
        print("** class name missing **")
    elif argl[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    elif len(argl) == 1:
        print("** instance id missing **")
    elif "{}.{}".format(argl[0], argl[1]) not in objdict:
        print("** no instance found **")
    else:
        print(objdict["{}.{}".format(argl[0], argl[1])])

def do_destroy(self, arg):
    """Delete a class instance of a given id"""
    argl = parse(arg)
    objdict = storage.all()
    if len(argl) == 0:
        print("** class name missing **")
    elif argl[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    elif len(argl) == 1:
        print("** instance id missing **")
    elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
        print("** no instance found **")
    else:
        del objdict["{}.{}".format(argl[0], argl[1])]
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
