#!/usr/bin/python3
"""User module"""


from models.base_model import BaseModel
import models


class User(BaseModel):
    """User class inherited from Basemodule"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """String representation of a User's instance"""

        return ("[User] ({}) {}".format(self.id, self.__dict__))
