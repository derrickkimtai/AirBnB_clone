#!/usr/bin/python3
"""Review Module"""


from models.base_model import BaseModel
import models


class Review(BaseModel):
    '''after visite a place we must check reviews about it'''
    place_id = ""
    user_id = ""
    text = ""

    def __str__(self):
        """String representation of a Review's instance"""
        return ("[Review] ({}) {}".format(self.id, self.__dict__))
