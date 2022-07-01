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
from models import storage

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
        if len(arg) == 0:
            print ('** class name missing **')
        args = arg.split()
        if len(args) == 1 and args[0] not in HBNBCommand.__classes:
            print ("** class doesn't exist **")
        elif len(args) == 1 and args[0] in HBNBCommand.__classes:
            print ('** instance id missing **')
        elif len(args) == 2 and args[0] in HBNBCommand.__classes:
            cl = args[0]
            id = args[1]
            key = cl+'.'+id
            aux = FileStorage.all(self)
            if key not in aux:
                print ('** no instance found **')
            else:    
                print (aux[key])


    def do_destroy(self, arg):
        """Delete a class instance of a given id"""

        argl = arg.split()
        objdict = FileStorage.all(self)
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
            FileStorage.save(self)

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""

        objdict = FileStorage.all(self)
        obj_list = []
        if len(arg) > 0:
            if arg not in HBNBCommand.__classes:
                print ("** class doesn't exist **")
            else:
                for item in objdict:
                    key = (item.split(sep='.'))[0]
                    if key == arg:
                        obj_list.append(str(objdict[item]))
                print (obj_list)
        else:
            for item in objdict:
                obj_list.append(str(objdict[item]))
            print (obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""

        args = arg.split()
        args_len = len(args)
        objdict = FileStorage.all(self)

        if args_len == 0:
            print ("** class name missing **")
        else:
            cl_name = args[0]
            if cl_name not in HBNBCommand.__classes:
                print ("** class doesn't exist **")
            else:
                if args_len == 1:
                    print ("** instance id missing **")
                else:
                    id_name = args[1]
                    key = cl_name+'.'+id_name
                    if args_len == 2:
                        print ("** attribute name missing **")
                    else:
                        at_name = args[2]
                        if args_len == 3:
                            print ("** value missing **")
                        else:
                             at_val = args [3]
                             key = cl_name+'.'+id_name
                             if key in objdict:
                                 setattr(objdict[key], args[2], args[3]) 
                                 FileStorage.save(self)
                             else:
                                 print ("** no instance found **")

    def default(self, arg):
        """ retrieve all instances of a class by using: <class name>.all()"""

        if (".all()") in arg:
            comm = arg.split(".all()")
            if comm[0] in HBNBCommand.__classes:
                HBNBCommand.do_all(self, comm[0])
            else:
                print("*** Invalid class: "+comm[0])
        else:
            print("*** Unknown syntax: "+arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()