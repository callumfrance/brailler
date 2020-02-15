from louis import translateString, backTranslateString
"""
Some possible tables:
    en-GB-g2.ctb
    en-gb-g1.utb
    en-us-g1.ctb
    en-us-g2.ctb

    More at:
        https://github.com/liblouis/liblouis/tree/master/tables
"""


class Reader:


    def get_input(console=True, fName=None):
        """Gets an input from either console or file and returns a list of strings
        """
        in_lines = list()
        if (not fName and not console) or (fName and console):
            raise ValueError("Invalid parameters to get_input()")
        elif console:
            in_lines = [input("\nConsole lines >").strip(),]
        elif fName:
            with open(fName, "r") as f:
                for line in f.readlines():
                    in_lines.append(line.strip())
        else:
            in_lines = ["This is a test string that can be used to write Braille.",]

        return(in_lines)


    @staticmethod
    def back_translate_item(in_str, t_tables=['unicode.dis', 'en-GB-g2.ctb']):
        """Translates a string from braille into unicode English
        """
        result = backTranslateString(t_tables, in_str)
        return(result)


    @staticmethod
    def translate_item(in_str, t_tables=['unicode.dis', 'en-GB-g2.ctb']):
        """Translates a string from unicode English into braille
        """
        result = translateString(t_tables, in_str)
        return(result)


    @staticmethod
    def print_translation(in_str):
        print(in_str)


    def reader_loop():
        """The main loop that chains together multiple reading commands
        """
        while True:
            console = choose_mode()
            fName = None
            if not console:
                fName = input("\nFile Name> ")
            x = get_input(console, fName)
            for i in x:
                y = translate_item(i)
                print_translation(y)
                pi_out_translation(y)


    def choose_mode():
        """Allows user to choose between reading from a console input
        or from a text file.
        """
        a = input("\nChoose your mode >")
        if a == '1':
            return(True)
        elif a == '2':
            return(False)
        else:
            choose_mode()


if __name__ == '__main__':
    reader_loop()
