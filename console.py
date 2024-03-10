#!/usr/bin/python3

"""
    This is is a file that creates a command line interpreter to run commands entered by
    the user and execute respective programs or classes associated with the command entered
    by the user
"""

import cmd
import ast
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
        This creates a command line interpreter that accepts users input and execute respective
        programs linked to the user input, e.g., command create, will create a new User object
    """
    
    prompt = '(hbnb) '
    
    correct_classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def do_create(self, arg):
        """ Create an object / instantiate an object """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            if args[0] in self.correct_classes.keys():
                obj = self.correct_classes[args[0]](args[1:])
            else:
                return
            obj.save()
            print(obj.uid)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Display all the entries or data stored in the file storage """
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) != 2 or args[0] not in self.correct_classes:
            print("** invalid syntax or class name missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")


    def do_destroy(self, arg):
        """ Delete an object that is stored in the file storage """
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) != 2 or args[0] not in self.correct_classes:
            print("** invalid syntax or class name missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Print all data stored in the file storage object """
        from models import storage
        args = arg.split()
        if not arg or args[0] == "":
            for obj in storage.all().values():
                print(str(obj))
        elif args[0] not in self.correct_classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all()[args[0]].values():
                print(str(obj))

    def do_update(self, arg):
        """ Update single data or entry to the file storage object (JSON) """
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(',')
        if len(args) != 3:
            print("** invalid number of arguments **")
            return
        class_id, dic_str = args[0], args[1].strip()
        if class_id not in self.correct_classes:
            print("** class doesn't exist **")
            return
        if len(class_id) == 0:
            print("** instance id missing **")
            return
        if len(dic_str) == 0:
            print("** dictionary missing **")
            return
        key = f"{class_id}.{args[0].split()[0]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        try:
            obj_dic = ast.literal_eval(dic_str)
        except ValueError:
            print("** invalid dictionary **")
            return
        for k, v in obj_dic.items():
            setattr(storage.all()[key], k, v)
        storage.save()

        
    def do_count(self, arg):
        """ Count the objects created """
        from models import storage
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.correct_classes:
            print("** class doesn't exist **")
            return
        print(len(storage.all()[args[0]]))

    def emptyline(self):
        """ Manage empty lines: Do Nothing incase of empty lines """
        pass

    def do_quit(self, arg):
        """ Quit the command line interpreter """
        return True

    def do_EOF(self, arg):
        """ Manage the End of File for the command line interpreter """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
    
    
    