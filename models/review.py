#!/usr/bin/python

"""
    This file contains the class / blueprint for the review objects which
    inherits some of it's attributes and methods from the BaseModel class
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.user import User
from models.place import Place

class Review(Place):
    """ Initializes the attributes for the Review class """
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = Place().uid
        self.user_id = Place().user_id
        self.text = text
