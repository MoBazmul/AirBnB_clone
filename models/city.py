#!/usr/bin/python3
"""
Defines the City class
"""

import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.base_model import BaseModel

class City(BaseModel):
    """City class inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
