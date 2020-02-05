"""
a view class
"""


class View:


    @staticmethod
    def option_select(in_options):
        """Given a list of strings, prints the list and waits for an integer in.
        """
        print("")
        for n, i in enumerate(in_options):
            print(n, ":", i)
        try:
            ans = int(input("\n> "))
        except ValueError: # If an bad value was provided, exit with None
            ans = None

        if ans < 0 or ans > len(in_options):
            ans = option_select(in_options)

        return(ans)


    @staticmethod
    def str_print(in_str):
        """Prints a provided string
        """
        print("Called view.str_print")
        print(in_str)
