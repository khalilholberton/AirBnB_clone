#!/usr/bin/python3
'''
create class to store object
'''


import json
import models
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    ''' class file storage'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''funct all'''
        return (FileStorage.__objects)

    def new(self, obj):
        ''' dic form'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''save'''
        save_file = self.__file_path
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(save_file, "w", encoding='utf-8') as F:
            json.dump(dic, F)

    def reload(self):
        '''relod'''
        dic = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                dic = json.load(f)
                for key, value in dic.items():
                    ob = eval(value['__class__'])(**value)
                    self.__objects[key] = ob
        except:
            pass
