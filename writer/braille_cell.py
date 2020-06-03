"""
The BrailleCell class is used to represent a single Braille cell object.

It provides tools so that it can check itself to see if it is blank,
translate itself into the unicode format, and check equivalency.
"""
import writer.write as write


class BrailleCell:


    def __init__(self, in_cell=[ False * 6 ]):
        self.cell = in_cell
        self.isBlank = True
        self.isFull = False
        self.blankFullCheck()

    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, in_cell):
        for i in in_cell[:6]:
            in_cell[i] = bool(in_cell[i])
        self._cell = in_cell
        self.blankFullCheck()

    def blankFullCheck(self):
        """ Boolean determinator for knowing if this BrailleCell has not dots
        Also checks to see if the cell is completely dotted out (i.e. strikethrough)
        """
        self.isBlank = True
        self.isFull = True
        for i in self.cell:
            if i:
                self.isBlank = False
                break
        for i in self.cell:
            if not i:
                self.isFull = False
                break

    def braille2unicode(self):
        """For the cell pattern, returns the unicode character representation
        """
        return(write.Writer().braille2unicode(self))

    def __eq__(self, other):
        if not isinstance(self, other.__class__):
            print("BC not eq at isinstance")
            return False
        else:
            for n, i in enumerate(self.cell):
                if other.cell[n] != self.cell[n]:
                    print("BC not eq at", n, other.cell[n], self.cell[n])
                    print(self.cell)
                    return False

        return True
