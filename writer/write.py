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


'Braille'    : an object that contains a _list_ of Braille
                '1 4'
                '2 5'
                '3 6'
'Binary_Str' : the binary string representation of a Braille cell
                '654321'
'Int'        : the integer representation of the binary string (0 - 63)

"""
import writer.braille_cell as braille_cell
import brailler.reader.read as read


class Writer:


    @staticmethod
    def binary_str2int(in_binary_str):
        """Converts a string of binary into an integer
        e.g. "101" --> 5
        e.g. "101101101" --> 365
        """
        return(int(in_binary_str, 2))

    @staticmethod
    def binary_str2braille(in_binary_str):
        """Converts a binary_str into a Braille object
        e.g. "100101" --> BrailleCell([True, False, True, False, False, True])
        """
        cells = [ False for i in range(6) ]
        for n, i in enumerate(in_binary_str[::-1]):
            if i == "1":
                cells[n] = True
        return(braille_cell.BrailleCell(cells))

    @staticmethod
    def braille2binary_str(in_cell):
        """For the cell pattern, returns the binary string representation
        e.g. BrailleCell([False, False, False, True, False, True])
                --> "101000"
        """
        b_str = ""
        for i in reversed(in_cell.cell):
            b_str += "1" if i else "0"
        return(b_str)

    @staticmethod
    def int2binary_str(in_int):
        """Converts an integer into a braille cell by looking at its bits.
        e.g. 5 --> "000101"
            (5 is '⠅')
        """
        if (in_int > 63) or (in_int < 0):
            raise ValueError("Braille integers must be from 0 to 63")
        out_cell = ""
        tester = in_int
        for i in range(6):
            if tester % 2 != 0:
                out_cell = "1" + out_cell
            else:
                out_cell = "0" + out_cell
            tester = tester >> 1
        return(out_cell)


    @staticmethod
    def braille2int_b(in_cell):
        """Converts a BrailleCell boolean list object into an integer
        representation of Braille.
        """
        return(Writer.binary_str2int(Writer.braille2binary_str(in_cell)))

    @staticmethod
    def braille2int_uni(in_cell):
        """Converts a BrailleCell boolean list object into an integer
        representation within the unicode system.
        """
        b_str = ""
        for i in reversed(in_cell.cell):
            b_str += "1" if i else "0"
        print(b_str)
        b_int = Writer.binary_str2int(b_str)
        return(10240 + b_int)

    @staticmethod
    def braille2unicode(in_cell):
        return(chr(Writer.braille2int_uni(in_cell)))

    @staticmethod
    def write_in(in_braille_str):
        """Converts a string of braille characters into a string of alphabeticals
        """
        return(read.Reader().back_translate_item(in_braille_str))
