import pytest

import os
import pprint

pprint.pprint(os.sys.path)

from brailler.writer.braille_cell import BrailleCell


def test_BrailleCell_default():
    b = BrailleCell()
    assert b.cell == [False * 6]

def test_BrailleCell_braille2unicode():
    code = [False, True, True, False, True, True]
    b = BrailleCell(code)
    assert b.braille2unicode() == '⠶'
