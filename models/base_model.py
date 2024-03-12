#!/usr/bin/python3
"""
Custom base class for the entire project
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

import uuid
from datetime import datetime

class BaseModel:
    """ Initializing the attributes that will be used by sub-classes that will
    inherit from this base class"""
    
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            for key in kwargs:
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        kwargs[key] = BaseModel.get_date_and_time()
                    setattr(self, key, kwargs[key])

            if 'created_at' not in kwargs:
                self.created_at = BaseModel.get_date_and_time()
            if 'updated_at' not in kwargs:
                self.updated_at = BaseModel.get_date_and_time()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = BaseModel.get_date_and_time()
            self.updated_at = BaseModel.get_date_and_time()
            storage.new(self)
            
    @classmethod
    def get_date_and_time(cls):
        """ Getting the date and time """
        return datetime.now().isoformat()

    def save(self):
        """ Save any changes made to the dictionary to the file-storage object """
        from models import storage
        self.updated_at = BaseModel.get_date_and_time()
        storage.save()

    def to_dict(self):
        """ changes the file-storage contents to dictionary """
        dictionary = self.__dict__.copy()
        
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at
        dictionary['updated_at'] = self.updated_at
        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
