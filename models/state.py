#!/usr/bin/python3
"""
Defines the State class
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.base_model import BaseModel

class State(BaseModel):
    """State class inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
