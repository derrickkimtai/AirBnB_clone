#!/usr/bin/python3
"""State Module"""


from models.base_model import BaseModel
import models


class City(BaseModel):
    """City Class iherited from Basemodel"""
    state_id = ""
    name = ""

    def __str__(self):
        """String representation of City instance"""

        return ("[City] ({}) {}".format(self.id, self.__dict__))
