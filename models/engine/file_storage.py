#!/usr/bin/python3

"""
    This file defines functions that are used to manipulate the storage to
    where the data in form of dictionaries are stored to file storages, using
    the json file mechanism
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "../../file.json"
    __objects = {}

    def all(self):
        """ Return the objects or data retrieved from the file storage """
        return self.__objects

    def new(self, instance):
        """ Create new entry or data to the object """
        key = f"{instance.__class__.__name__}.{instance.uid}"
        self.__objects[key] = instance

    def save(self):
        """ Save any changes made to the __objects dict to file storage """
        objects_to_be_saved = {}
        for key in self.__objects:
            objects_to_be_saved[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(objects_to_be_saved, file)

    def reload(self):
        """ Reload the data that was saved in the File Storage """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)
                for key in loaded_data:
                    class_name, obj_id = key.split('.')
                    class_dict = loaded_data[key]
                    
                    if '__class__' in class_dict:
                        class_name = class_dict['__class__']
                        instance_class = eval(class_name)
                    else:
                        instance_class = BaseModel
                    instance = instance_class(**class_dict)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
