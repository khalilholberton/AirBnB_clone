#!/usr/bin/python3

from models.base_model import BaseModel

'''user '''


class User(BaseModel):
    '''manage user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
