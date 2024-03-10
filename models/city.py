#!/usr/bin/python

"""
    This file contains the class / blueprint for the city objects which
    inherits some of it's attributes and methods from the BaseModel class
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.state import State

class City(State):
    """ Initializes the attributes for the City class """
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = State().uid
        self.name = name
        
        
if __name__ == '__main__':
    city = City('Mombasa')
    print(city)       
        
