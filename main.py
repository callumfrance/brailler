"""
Main

The input-independent means of controlling the brailler program
"""
from os import listdir
from os.path import isfile, isdir, join

from views.view import View
from reader.read import *

# TODO possible refactor into a database value or something
user_path = 'user'
view = None

def setup():
    """Code that should only run once when the program is launched.

    Check the raspberry pi connections.
    Check that the relevant libraries have been installed.
    Check that the user_path 'user' folder exists
    """
    global view

    if not isdir(user_path): # Check that the user_path 'user' folder exists
        os.mkdir(user_path)
        if not isdir(user_path):
            raise OSError("Could not create the user_path directory")

    view = View()


def teardown():
    """Code that should only run once when the program is to be exited.
    """
    pass


def menu_read_file(user_path='user'):
    """Allows user to select a file to read from within the user_path
    """
    # TODO only get text files (not binary files) -- use mimetype library
    view_select = None
    brailleTextFile = False
    only_files = list()
    first_char_test = ''

    only_files = [f for f in listdir(user_path) if isfile(join(user_path, f))]
    view.str_print(only_files)
    view_select = view.option_select(only_files)

    if view_select == None: # User decided to not read any of the files
        return None
    else: # User has selected a file to read from - now determine the 'language'
        with open(user_path + "/" + only_files[view_select], 'r') as f:
            first_char_test = f.read(1)
            if ord(first_char_test) >= 10240 or ord(first_char_test) <= 10303:
                brailleTextFile = True
            else:
                brailleTextFile = False
            y = first_char_test + f.read()
            x = translate_item(y)
            view.str_print(x)
            view.str_print(y)


def menu_write_file(user_path='user'):
    """Allows user to create a file to write to within the user_path
    """
    only_files = [f for f in listdir(user_path) if isfile(join(user_path, f))]
    
    view.str_print("Enter a new file name to write to:")
    new_file_name = view.str_input() # TODO handling of inner and outer folders....

    encoding = view.option_select(["No text translation", 
        "US Braille translation", 
        "UK Braille translation", 
        "Decide once completed",])

    if new_file_name in only_files:
        view.str_print("This file already exists")
    else:
        user_input = view.str_input()
        if encoding == 3:
            encoding = view.option_select(["No text translation", 
                "US Braille translation", 
                "UK Braille translation",])
        if encoding == 1:
            pass # TODO perform translations before write to file here
        elif encoding == 2:
            pass
        with open(user_path + "/" + new_file_name, "x") as f:
            f.write(user_input)


def menu(user_path='user'):
    """Allows user to choose a menu option
    """
    function_choice = ["Read a file", "Write a new file",]
    view_select = view.option_select(function_choice)

    if view_select == 0: # Read a file
        menu_read_file()
    elif view_select == 1: # Write a new file
        menu_write_file()

    return(None)


def main_loop():
    to_exit = False
    while not to_exit:
        menu()


if __name__ == '__main__':
    setup()
    main_loop()
    teardown()
