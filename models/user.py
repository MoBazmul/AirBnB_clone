#!/usr/bin/python3
"""
Defines the User class.
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.base_model import BaseModel

class User(BaseModel):
    """User class inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
