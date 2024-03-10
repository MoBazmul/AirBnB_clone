#!/usr/bin/python3

""" 
    This class acts as a blueprint to all other classes that will have to
    initialize and use common attributes and methods defined in this class.
    Basically, it will act as a parent class to all sub-classes that will 
    need to inherit from this super class (BaseModel) 
"""

import uuid
import datetime

class BaseModel:
    
    def __init__(self, *args, **kwargs):
        """ Initializes the instances that will be created from the BaseModel class
            Checks if passed keys to the keywords args (**kwargs) exists in the initial
            created dictionary, if it does not exist, initializes the keys from the **kwargs
            argument
        """
        if kwargs:
            for key in kwargs:
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        kwargs[key] = self.get_datetime()
                    setattr(self, key, kwargs[key])
                    
            if 'created_at' not in kwargs:
                self.created_at = self.get_datetime()
            if 'updated_at' not in kwargs:
                self.updated_at = self.created_at
                
        self.uid = str(uuid.uuid4())
        self.created_at = self.get_datetime()
        self.updated_at = self.created_at 
        
    @classmethod
    def copy(cls, dict1, dict2):
        """ Copy the contents of one dictionary to another """
        for key, value in dict1.items():
            dict2[key] = value
        return dict2
    
    @classmethod
    def get_datetime(cls):
        """ Get the date and time """
        datetime_ = datetime.datetime.now().isoformat()
        return str(datetime_)
        
    def save(self):
        from models import storage
        """ Save changes made to the File Storage """
        self.created_at = self.get_datetime()
        storage.save()
        
    def to_dict(self):
        """ Changes an object (class_dict) to a dictionary object """
        dictionary = {}
        dictionary = self.copy(self.__dict__, dictionary)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at
        dictionary['updated_at'] = self.updated_at
        return dictionary
        
    def __str__(self):
        """ Prints object's properties """
        return f"""
            [<{self.__class__.__name__}>]
            ({self.uid})
            <{self.__dict__}>
        """

if __name__ == '__main__':
    base = BaseModel(name = 'Mohammed', age = 25)
    print(base.to_dict())

