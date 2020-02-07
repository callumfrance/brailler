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
# from writer.braille_cell import BrailleCell
from reader.read import back_translate


class Writer:


    @staticmethod
    def binary_str2int(in_binary_str):
        """Converts a string of binary into an integer
        e.g. "101" --> 5
        e.g. "101101101" --> 365
        """
        ans = 0
        for n, i in in_binary_str:
            ans += int(i) * (1 << n)
        return(ans)

    @staticmethod
    def int2braille(in_int):
        """Converts an integer into a braille cell by looking at its bits.
        e.g. 5 --> [True, False, True]
        """
        if (a > 63) or (a < 0):
            raise ValueError("Braille integers must be from 0 to 63")
        out_cell = BrailleCell([False for i in range(6)])
        tester = in_int
        for i in range(6):
            if tester % 2 == 0:
                out_cell.cell[i] = True
            tester = tester >> 1
        return(out_cell)

    @staticmethod
    def braillel2binary_str(in_cell):
        """For the cell pattern, returns the binary string representation
        """
        b_str = ""
        for i in in_cell:
            b_str += "1" if i else "0"
        return(b_str)

    @staticmethod
    def braille2int(in_cell):
        """Converts a BrailleCell boolean list object into an integer
        """
        return(binary_str2int(braille2binary_str(in_cell)))

    @staticmethod
    def braille2unicode(in_cell):
        return(chr(braille2int(in_cell)))

    @staticmethod
    def write_in(in_braille_str):
        """Converts a string of braille characters into a string of alphabeticals
        """
        return(back_translate(in_braille_str))
