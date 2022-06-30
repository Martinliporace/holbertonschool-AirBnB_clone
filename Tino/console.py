#!/usr/bin/python3
"""Defines the console."""
import cmd, sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Defines the Holberton command interpreter"""

    prompt = '(hbnb) '

    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
            }

    def emptyline(self):
        """Do nothing receiving an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            BaseModel.save(self)

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id
        """
        key = arg.split()[0]+'.'+arg.split()[1]
        aux = FileStorage.all(self)
        print (aux[key])


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