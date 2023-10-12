#!/usr/bin/python3
"""Place Module"""


from models.base_model import BaseModel
import models


class Place(BaseModel):
    '''place attributes'''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __str__(self):
        """representation of a Place's instance by using magic method"""

        return ("[Place] ({}) {}".format(self.id, self.__dict__))
