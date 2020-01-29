from louis import translate


def get_input(console=True, fName=None):
    in_lines = ""
    if (not fName and not console) or (fName and console):
        raise ValueError("Invalid parameters to get_input()")
    elif console:
        in_lines = [input("\nConsole lines >"),]
    elif fName:
        with open(fName, "r") as f:
            in_lines = f.readlines()
    else:
        in_lines = ["This is a test string that can be used to write Braille.",]

    return(in_lines)


def translate_item(in_str, t_tables=['unicode.dis', 'en-GB-g2.ctb']):
    result = translate(t_tables, in_str)
    return(result[0])


def print_translation(in_str):
    print(in_str)


def pi_out_translation(in_str):
    pass


def reader_loop():
    while True:
        console = choose_mode()
        fName = None
        if not console:
            fName = input("\nFile Name> ")
        x = get_input(console, fName)
        for i in x:
            y = translate_item(x)
            print_translation(y)
            pi_out_translation(y)


def choose_mode():
    a = input("\nChoose your mode >")
    if a == '1':
        return(True)
    elif a == '2':
        return(False)
    else:
        choose_mode()


if __name__ == '__main__':
    reader_loop()
