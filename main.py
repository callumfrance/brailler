"""
Main

The input-independent means of controlling the brailler program
"""
from os import listdir
from os.path import isfile, isdir, join

from views.view import View

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
    print(view)


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
    file_reader_obj = None
    only_files = [f for f in listdir(user_path) if isfile(join(user_path, f))]
    print(only_files)
    view_select = view.option_select(only_files)
    # view_select = 1
    if view_select == None: # User decided to not read any of the files
        return None
    else: # User has selected a file to read from - now determine the 'language'
        with open(user_path + "/" + only_files[view_select], 'r') as f:
            first_char_test = f.read(1)
            if ord(first_char_test) >= 10240 or ord(first_char_test) <= 10303:
                brailleTextFile = True
            else:
                brailleTextFile = False
            print(first_char_test + f.read())
    # TODO use the information gathered from this method to create an object
    #   that contains all the necessary information to read a file with
    return(file_reader_obj)


def menu(user_path='user'):
    """Allows user to choose a menu option
    """
    function_choice = ["Read a file", "Write a new file",]
    view_select = view.option_select(function_choice)
    # view_select = 1

    if view_select == 0: # Read a file
        menu_read_file()
    elif view_select == 1: # Write a new file
        # TODO menu_write_file()
        pass

    return(None)


def main_loop():
    to_exit = False
    while not to_exit:
        menu()


if __name__ == '__main__':
    setup()
    main_loop()
    teardown()
