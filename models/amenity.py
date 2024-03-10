#!/usr/bin/python

"""
    This file contains the class / blueprint for the amenity objects which
    inherits some of it's attributes and methods from the BaseModel class
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Initializes the attributes for the Amenity class """
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        
if __name__ == '__main__':
    amenity = Amenity('Wifi')
    print(amenity)
