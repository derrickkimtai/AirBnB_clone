#!/usr/bin/python3
"""[BaseModel Module]
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Basemodel of AirBnb project"""

    def __init__(self, *args, **kwargs):
        """constructor of BaseModel:
        *args : Unused (because we handling the dictionary forme key/Value).
        **kwargs (dict): Key/value represent attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue

                if k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.strptime(v,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        dic_obj = self.__dict__.copy()
        dic_obj["__class__"] = self.__class__.__name__
        dic_obj["updated_at"] = self.updated_at.isoformat()
        dic_obj["created_at"] = self.created_at.isoformat()

        return dic_obj

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
