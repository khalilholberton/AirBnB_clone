#!/usr/bin/python3
'''
this module contain  class BaseModel
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    that defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        """init"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key in ['updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """
        function to_dict
        """

        dic = {}
        for key, value in self.__dict__.items():
            if key != 'created_at' and key != 'updated_at':
                dic[key] = value

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

    def save(self):
        """
        fucntion save
        """

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """function str"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
