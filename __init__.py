# dbdb/__init__.py
from interface import DBDB
import os

def establish_connection(database_name):
    try:
        file_handle = open(database_name, 'r+b')
    except IOError:
        file_descriptor = os.open(database_name, os.O_RDWR | os.O_CREAT)
        file_handle = os.fdopen(file_descriptor, 'r+b')
    
    return DBDB(file_handle)
