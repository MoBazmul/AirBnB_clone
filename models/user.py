#!/usr/bin/python

"""
    This file contains the class / blueprint for the user objects which
    inherits some of it's attributes and methods from the BaseModel class
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.base_model import BaseModel

class User(BaseModel):
    """ Initializes the attributes for the User class """
    def __init__(self, email, password, first_name, last_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        
        
if __name__ == '__main__':
    user = User('mohaarash001@gmail.com', 'baz0001', 'Mohammed', 'Bazmul')
    print(user)    
    

