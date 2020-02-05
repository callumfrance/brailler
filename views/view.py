"""
a view class
"""


view_types = ['CLI',]


class View:


    def __init__(self, view_type='CLI'):
        self.view_type = view_type

    @staticmethod
    def option_select(in_options):
        """Given a list of strings, prints the list and waits for an integer in.
        """
        View.str_print("")
        for n, i in enumerate(in_options):
            View.str_print(str(n) + " : " + i)
        try:
            ans = int(View.str_input("\n> "))
        except ValueError: # If an bad value was provided, exit with None
            ans = None

        if ans < 0 or ans > len(in_options):
            ans = option_select(in_options)

        return(ans)

    @staticmethod
    def str_print(in_str, ender="\n"):
        """Prints a provided string

        This is the most basic type of printing in this program.
        Replaces `print()`.
        """
        # TODO filter off into the different printing types (i.e. self.view_type)
        print(in_str, end=ender)

    @staticmethod
    def str_input(inputter="\n> "):
        """Gets and then returns a string from the user.

        The returned string should always be in alphabetical, not braille.
        This is because the program may need to logically understand the input.

        This is the most basic type of inputting in this program.
        Replaces `input()`.
        """
        x = input(inputter)
        # TODO process a translation depending on the type of input received
        return(x)
