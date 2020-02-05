"""
How to write from braille:

    <<You have a list of six bools>>

1. Read the boolean mappings from database or something (SymbolData...)
2. Find the matching index number according to braille binary
3. Return the braille cell in unicode at that index value

    <<You now have a unicode braille cell>>

4. Repeat until you have read a word (i.e. until space, newline, EOF detected)

    <<You now have a braille (phrase or) word>>

5. Turn the braille word into an english unicode word using louis.backTranslate
6. Print, retaining whitespace deliminations
"""


def binary_str2int(in_binary_str):
    """Converts a string of binary into an integer
    e.g. "101" --> 5
    e.g. "101101101" --> 365
    """
    ans = 0
    for n, i in in_binary_str:
        ans += int(i) * (1 << n)
    return(ans)


def int2braille(in_int):
    """Converts an integer into a braille cell by looking at its bits.
    e.g. 5 --> [True, False, True]
    """
    if (a > 63) or (a < 0):
        raise ValueError("Braille integers must be from 0 to 63")
    out_list = [False for i in range(6)]
    tester = in_int
    for i in range(6):
        if tester % 2 == 0:
            out_list[i] = True
        tester = tester >> 1
    return(out_list)


def write_in(in_braille_str):
    """Converts a string of braille characters into a string of alphabeticals
    """
    # reader.back_translate
    pass
