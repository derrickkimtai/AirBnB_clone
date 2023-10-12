#!/usr/bin/python3
"""Amenity module"""


from models.base_model import BaseModel
import models


class Amenity(BaseModel):
    '''every one lokking for amenity'''
    name = ''

    def __str__(self):
        return ("[City] ({}) {}".format(self.id, self.__dict__))
