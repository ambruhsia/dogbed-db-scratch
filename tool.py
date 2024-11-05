import sys
import os
import dbdb
 
def process_command_line_args(arguments):
    if not (4 <= len(arguments) <= 5):
        show_usage()
        return ARGUMENTS_ERROR
    
    db_name, action, key, value = (arguments[1:] + [None])[:4]
    
    if action not in {'get', 'set', 'delete'}:
        show_usage()
        return INVALID_ACTION

    database = dbdb.connect(db_name)  # Establishing database connection

    try:
        if action == 'get':
            sys.stdout.write(database[key])  # Retrieving the value
        elif action == 'set':
            database[key] = value  # Setting a new value
            database.commit()
        elif action == 'delete':
            del database[key]  # Deleting the key-value pair
            database.commit()
    except KeyError:
        print("The specified key was not found", file=sys.stderr)
        return KEY_NOT_FOUND_ERROR
    
    return SUCCESS

# Helper function to display usage
def show_usage():
    print("Usage: <db_name> <action: get/set/delete> <key> [value]")

# Constants for return codes
ARGUMENTS_ERROR = 1
INVALID_ACTION = 2
KEY_NOT_FOUND_ERROR = 3
SUCCESS = 0
