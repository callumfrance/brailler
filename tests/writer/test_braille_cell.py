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

def test_BrailleCell__eq__():
    a = BrailleCell()
    b = BrailleCell()
    c = BrailleCell([ False, True, False, True, False, True ])
    d = BrailleCell([ False, False, False, True, False, True ])

    assert a == b
    assert c != d
    assert d != ('Tuple', 'Not', 'BrailleCell')
    assert a != None
    assert a == BrailleCell([ False, False, False, False, False, False ])
    assert a == BrailleCell([ False * 6 ])
    assert a == BrailleCell([ False for i in range(6) ])
