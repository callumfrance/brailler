import abc


class ViewType(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def option_select(self):
        """Given a list of strings, prints the list and waits for an integer in.
        """
        pass

    @abc.abstractmethod
    def str_print(self):
        """Prints a provided string

        This is the most basic type of printing in this program.
        Replaces `print()`.
        """
        pass

    @abc.abstractmethod
    def str_input(self):
        """Gets and then returns a string from the user.

        The returned string should always be in alphabetical, not braille.
        This is because the program may need to logically understand the input.

        This is the most basic type of inputting in this program.
        Replaces `input()`.
        """
        pass

