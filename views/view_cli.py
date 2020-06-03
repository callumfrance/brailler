"""
This is the ViewCLI class, used to interface this program via
the console (e.g. terminal, commandline, or shell).

This class can be used to demonstrate the functionality of the ViewBraille
class on a computer via the shell.

Despite being referred to as a 'view' it also includes support for input.
"""

class ViewCLI:


    @staticmethod
    def option_select(in_options):
        """Given a list of strings, prints the list and waits for an integer in.
        """
        ViewCLI.str_print("")
        for n, i in enumerate(in_options):
            ViewCLI.str_print(str(n) + " : " + i)
        try:
            ans = int(ViewCLI.str_input("\n> "))
        except ValueError: # If an bad value was provided, exit with None
            ans = None

        if ans < 0 or ans > len(in_options):
            ans = None

        return(ans)

    @staticmethod
    def str_print(in_str, ender="\n"):
        """Prints a provided string

        This is the most basic type of printing in this program.
        Replaces `print()`.
        """
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

