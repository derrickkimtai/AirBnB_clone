#!/usr/bin/python3
"""State Module"""


from models.base_model import BaseModel
import models


class State(BaseModel):
    """State inhereted from Basemodel for HBnB"""
    name = ""

    def __str__(self):
        """String representation of state """
        return ("[State] ({}) {}".format(self.id, self.__dict__))
