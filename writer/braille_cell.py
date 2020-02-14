import brailler.writer.write


class BrailleCell:


    def __init__(self, in_cell=[ False * 6 ]):
        self.cell = in_cell

    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, in_cell):
        for i in in_cell[:6]:
            in_cell[i] = bool(in_cell[i])
        self._cell = in_cell

    def braille2unicode(self):
        """For the cell pattern, returns the unicode character representation
        """
        return(write.Writer.braille2unicode(self.cell))

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
