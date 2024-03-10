#!/usr/bin/python

"""
    This file contains the class / blueprint for the place objects which
    inherits some of it's attributes and methods from the BaseModel class
"""
import sys

sys.path.append('/home/mohammed/Desktop/AirBnB_clone')

from models.user import User
from models.city import City

class Place(User, City):
    """ Initializes the attributes for the Place class """
    def __init__(self, name, description, number_rooms=0, number_bathrooms=0, max_guest=0, price_by_night=0, latitude=0.0, longitude=0.0, amenity_ids=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = City().uid
        self.user_id = User().uid
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
        
        
if __name__ == '__main__':
    place = Place('80100', 'u89u382989912812', 'Villa Peponi', 'Amazing Place', 6, 16, 10, 5000, 23423413.2323, 32143432.21342, ['hello', 'id1', 'id2'])
    print(place)
        
        
    