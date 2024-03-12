#!/usr/bin/python3
"""
Defines the Review class.
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")

