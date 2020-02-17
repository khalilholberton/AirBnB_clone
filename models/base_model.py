#!/usr/bin/python3
'''create class basemodel'''
import uuid
from datetime import datetime


class BaseModel:
    '''that defines all common attributes/methods for other classes'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = {}
        for key, value in self.__dict__.items():
            if key != 'created_at' and key != 'updated_at':
                dic[key] = value
        
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
       
        return dic
    

    def save(self):
        self.updated_at = datetime.now()

    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
