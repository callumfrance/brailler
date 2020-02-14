import pytest

import os
import pprint

pprint.pprint(os.sys.path)

from brailler.writer.braille_cell import BrailleCell

def test_class():
    b = BrailleCell()
    assert b.cell == [False * 6]
