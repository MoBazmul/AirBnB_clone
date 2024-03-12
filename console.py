#!/usr/bin/python3

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    
    prompt = '(hbnb) '
    
    classes = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
        'User': User
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to the JSON file, and print the id."""
        if not arg:
            print("** class name missing **")
            return

        class_name, *attributes = arg.split()

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()

        if attributes:
            for attribute in attributes:
                attr_name, attr_value = attribute.split("=")
                setattr(new_instance, attr_name, attr_value)

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of instances"""
        from models import storage
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return
        if arg not in storage.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in storage.all().items() if key.split('.')[0] == arg])

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** dictionary missing **")
            return
        try:
            update_dict = eval(args[2])
            if not isinstance(update_dict, dict):
                raise SyntaxError
        except SyntaxError:
            print("** invalid dictionary **")
            return
        for k, v in update_dict.items():
            setattr(objects[key], k, v)
        storage.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        from models import storage
        if "(" in line and ")" in line:
            parts = line.split("(")
            command = parts[0]
            params = parts[1][:-1]
            if '.' in command:
                class_name, method = command.split('.')
                if hasattr(storage.classes.get(class_name), method):
                    if 'show' in method:
                        self.do_show(params)
                    elif 'count' in method:
                        self.do_count(params)
                    elif 'all' in method:
                        self.do_all(params)
            else:
                print("*** Unknown syntax: {}".format(line))

    def do_count(self, arg):
        """Count the number of instances of a class"""
        from models import storage
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all().keys() if key.split('.')[0] == arg)
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

