#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class FileStorage:
    """Class for managing serialization and deserialization of instances to JSON file."""
    
    __file_path = "file.json"
    __objects = {}

    classes = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
        'User': User
    }

    def all(self):
        """Return dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add new object to storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects and save to JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file, indent=2)

    def reload(self):
        """ Reload data from the storage """
        try:
            with open(self.__file_path, 'r') as file:
                # Check if the file is empty
                if os.stat(self.__file_path).st_size == 0:
                    return
                loaded_objects = json.load(file)
                for key in loaded_objects:
                    obj_class = BaseModel  # Default to BaseModel if class name is not recognized
                    class_name = key.split('.')[0]
                    
                    match class_name:
                        case "State":
                            obj_class = State
                        case "City":
                            obj_class = City
                        case "Amenity":
                            obj_class = Amenity
                        case "Place":
                            obj_class = Place
                        case "Review":
                            obj_class = Review
                    obj = obj_class(**loaded_objects[key])
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
        
        
