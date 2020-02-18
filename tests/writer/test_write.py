import pytest

import brailler.writer.write as write
import writer.braille_cell as braille_cell


def test_Writer_default():
    w = write.Writer()
    assert isinstance(w, write.Writer) == True


def test_Writer_binary_str2int():
    eg1 = "100000"
    ans_eg1 = 32

    eg2 = "001011"
    ans_eg2 = 32

    eg3 = "000000"
    ans_eg3 = 32

    w = write.Writer()
    assert w.binary_str2int(eg1) == 32
    assert w.binary_str2int(eg2) == 11
    assert w.binary_str2int(eg3) == 0

def test_Writer_binary_str2braille():
    eg1 = "100000"
    ans_eg1 = braille_cell.BrailleCell([ False, False, False, False, False, True ])
    eg2 = "001011"
    ans_eg2 = braille_cell.BrailleCell([ True, True, False, True, False, False ])
    eg3 = "000000"
    ans_eg3 = braille_cell.BrailleCell([ False for i in range(6) ])

    w = write.Writer()
    assert w.binary_str2braille(eg1).cell == ans_eg1.cell
    assert w.binary_str2braille(eg2).cell == ans_eg2.cell
    assert w.binary_str2braille(eg3).cell == ans_eg3.cell
    assert w.binary_str2braille(eg1) == ans_eg1
    assert w.binary_str2braille(eg2) == ans_eg2
    assert w.binary_str2braille(eg3) == ans_eg3

def test_Writer_braille2binary_str():
    ans_eg1 = "100000"
    eg1 = braille_cell.BrailleCell([ False, False, False, False, False, True ])
    ans_eg2 = "001011"
    eg2 = braille_cell.BrailleCell([ True, True, False, True, False, False ])
    ans_eg3 = "000000"
    eg3 = braille_cell.BrailleCell([ False for i in range(6) ])

    w = write.Writer()
    assert w.braille2binary_str(eg1).cell == ans_eg1.cell
    assert w.braille2binary_str(eg2).cell == ans_eg2.cell
    assert w.braille2binary_str(eg3).cell == ans_eg3.cell

def test_Writer_int2binary_str():
    eg1 = 32
    ans_eg1 = "100000"

    eg2 = 11
    ans_eg2 = "001011"

    eg3 = 0
    ans_eg3 = "000000"

    w = write.Writer()
    assert w.int2binary_str(eg1) == ans_eg1
    assert w.int2binary_str(eg2) == ans_eg2
    assert w.int2binary_str(eg3) == ans_eg3


def test_Writer_braille2binary_str():
    eg1 = braille_cell.BrailleCell([ True, False, False, False, False, False ])
    ans_eg1 = "000001"

    eg2 = braille_cell.BrailleCell([ False, False, True, False, True, True ])
    ans_eg2 = "110100"

    eg3 = braille_cell.BrailleCell([ False for i in range(6) ])
    ans_eg3 = "000000"

    w = write.Writer()
    assert w.braille2binary_str(eg1) == ans_eg1
    assert w.braille2binary_str(eg2) == ans_eg2
    assert w.braille2binary_str(eg3) == ans_eg3


def test_Writer_braille2int_b():
    eg1 = braille_cell.BrailleCell([ False, False, False, False, False, True ])
    ans_eg1 = 32

    eg2 = braille_cell.BrailleCell([ True, True, False, True, False, False ])
    ans_eg2 = 11

    eg3 = braille_cell.BrailleCell([ False for i in range(6) ])
    ans_eg3 = 0

    w = write.Writer()
    assert w.braille2int_b(eg1) == ans_eg1
    assert w.braille2int_b(eg2) == ans_eg2
    assert w.braille2int_b(eg3) == ans_eg3


def test_Writer_braille2unicode():
    eg1 = braille_cell.BrailleCell([ True, False, False, False, False, False ])
    eg2 = braille_cell.BrailleCell([ False, False, True, False, True, True ])
    eg3 = braille_cell.BrailleCell([ False for i in range(6) ])
    eg4 = braille_cell.BrailleCell([ False, True, True, False, True, True ])
    eg5 = braille_cell.BrailleCell([ True, True, True, False, True, True ])
    eg6 = braille_cell.BrailleCell([ False, False, False, True, True, True ])
    eg7 = braille_cell.BrailleCell([ True, False, False, True, True, True ])
    eg8 = braille_cell.BrailleCell([ False, True, False, True, True, True ])
    eg9 = braille_cell.BrailleCell([ True, True, False, True, True, True ])

    ans_eg1 = '⠁' # 1
    ans_eg2 = '⠴' # 19
    ans_eg3 = '⠀' # 0
    ans_eg4 = '⠶' # 54
    ans_eg5 = '⠷' # 55
    ans_eg6 = '⠸' # 56
    ans_eg7 = '⠹' # 57
    ans_eg8 = '⠺' # 58
    ans_eg9 = '⠻' # 59

    w = write.Writer()
    assert w.braille2unicode(eg1) == ans_eg1
    assert w.braille2unicode(eg2) == ans_eg2
    assert w.braille2unicode(eg3) == ans_eg3
    assert w.braille2unicode(eg4) == ans_eg4
    assert w.braille2unicode(eg5) == ans_eg5
    assert w.braille2unicode(eg6) == ans_eg6
    assert w.braille2unicode(eg7) == ans_eg7
    assert w.braille2unicode(eg8) == ans_eg8
    assert w.braille2unicode(eg9) == ans_eg9

