#!/usr/bin/python

"""
    This file contains the class / blueprint for the state objects which
    inherits some of it's attributes and methods from the BaseModel class
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.base_model import BaseModel

class State(BaseModel):
    """ Initializing attributes for the class State """
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
    
if __name__ == '__main__':
    state = State('Bazmul')
    print(state.name)

