#!/usr/bin/python3
'''class file storage'''
import json


class FileStorage:
    '''create class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''funct all'''
        return(self.__objects)

    def new(self, obj):
        ''' dic form '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''save'''
        dic = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(dic, f)
        
    def reload(self):
        '''reload'''
        rload = {}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as F:
                rload = (json.load(F))
                for key, value in rload.items():
                    ob = eval(value['__class__'](**value))
                    self.__objects[key] = ob
        except:
            pass
                              

            
