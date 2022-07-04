#!/usr/bin/python3
"""Defines the console."""

import cmd
import sys
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

    if sys.stdin and sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)\n'

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
        """Create a new class instance and print its id
           ex: (hbnb) create User"""

        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """Display the string representation of
        a class instance of a given id
        ex: (hbnb) show <id>"""

        if len(arg) == 0:
            print('** class name missing **')
        args = arg.split()
        if len(args) == 1 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in HBNBCommand.__classes:
            print('** instance id missing **')
        elif len(args) == 2 and args[0] in HBNBCommand.__classes:
            cl = args[0]
            id = args[1]
            key = cl+'.'+id
            aux = FileStorage.all(self)
            if key not in aux:
                print('** no instance found **')
            else:
                print(aux[key])

    def do_destroy(self, arg):
        """Delete a class instance of a given id
           ex: (hbnb) destroy BaseModel 1234-1234-1234"""

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
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        ex: (hbnb) all Place"""

        objdict = FileStorage.all(self)
        obj_list = []
        if len(arg) > 0:
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                for item in objdict:
                    key = (item.split(sep='.'))[0]
                    if key == arg:
                        obj_list.append(str(objdict[item]))
                print(obj_list)
        else:
            for item in objdict:
                obj_list.append(str(objdict[item]))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        ex: (hbnb) update BaseModel 1234-1234-1234 email aibnb@mail.com"""

        args = arg.split()
        args_len = len(args)
        objdict = FileStorage.all(self)

        if args_len == 0:
            print("** class name missing **")
        else:
            cl_name = args[0]
            if cl_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                if args_len == 1:
                    print("** instance id missing **")
                else:
                    id_name = args[1]
                    key = cl_name+'.'+id_name
                    if key not in objdict:
                        print("** no instance found **")
                    if args_len == 2:
                        print("** attribute name missing **")
                    else:
                        at_name = args[2]
                        if args_len == 3:
                            print("** value missing **")
                        else:
                            arg_val = ''
                            list_str = ['email', 'password', 'first_name',
                                        'last_name', 'name', 'state_id',
                                        'city_id', 'user_id,description',
                                        'place_id', 'text']
                            list_float = ['latitude', 'longitude']
                            list_int = ['price_by_night', 'max_guest',
                                        'number_bathrooms', 'number_rooms']
                            list_list = ['amenity_ids']
                            tipo = type(eval(args[3]))
                            at_val = args[3]
                            tipo = type(at_val)
                            if args_len > 3 and ((args[3])[0]) == '"':
                                for i in range(3, args_len):
                                    arg_val += (str(args[i])+' ')
                                at_val = arg_val[1:-2]

                            key = cl_name+'.'+id_name
                            if key in objdict:
                                setattr(objdict[key], at_name, tipo(at_val))
                                storage.save()

    def default(self, arg):
        """ retrieve all instances of a class by using: <class name>.all()"""

        if (".all") in arg:
            cl = arg.split(".all()")
            if cl[0] in HBNBCommand.__classes:
                HBNBCommand.do_all(self, cl[0])
            else:
                print("*** Invalid class: "+cl[0])

        elif(".count") in arg:
            cont = 0
            cl = arg.split(".count()")
            if cl[0] in HBNBCommand.__classes:
                objdict = FileStorage.all(self)
                for i in objdict:
                    if cl[0] in i:
                        cont += 1
                print(cont)
            else:
                print("*** Invalid class: "+cl[0])

        elif(".show") in arg:
            cl = str(arg.split(".show")[0])
            id = str((arg.split("(")[1]).split(")")[0])
            parameter = cl+' '+id
            HBNBCommand.do_show(self, parameter)

        elif(".destroy") in arg:
            cl = str(arg.split(".destroy")[0])
            id = str((arg.split("(")[1]).split(")")[0])
            parameter = cl+' '+id
            HBNBCommand.do_destroy(self, parameter)

        elif(".update") in arg:
            cl = str(arg.split(".update")[0])
            bet_par = str((arg.split("(")[1]).split(")")[0])
            id = str(bet_par.split(",")[0])
            att_name = str(bet_par.split(",")[1])
            att_val = str(bet_par.split(",")[2])
            par = cl+' '+id+' '+att_name+' '+att_val
            bet_brack = str((arg.split("{")[1]).split("}")[0])
            tipo = type(bet_brack)
            dict_aux = dict(sub.split(':') for sub in bet_brack.split(','))
            if isinstance(dict_aux, dict) == True:
                for key, value in dict_aux.items():
                    par = cl+' '+id+' '+key.strip("\"'")+' '+value
                    HBNBCommand.do_update(self, par)
            else:
                HBNBCommand.do_update(self, par)

        else:
            print("*** Unknown syntax: "+arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
