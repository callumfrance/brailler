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
        ans = int(input("\n> "))

        if ans < 0 or ans > len(in_options):
            ans = option_select(in_options)

        return(ans)
