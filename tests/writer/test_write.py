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


def test_Writer_int2braille():
    eg1 = 32
    ans_eg1 = braille_cell.BrailleCell([ True, False, False, False, False, False ])

    eg2 = 11
    ans_eg2 = braille_cell.BrailleCell([ False, False, True, False, True, True ])

    eg3 = 0
    ans_eg3 = braille_cell.BrailleCell([ False for i in range(6) ])

    w = write.Writer()
    assert w.int2braille(eg1) == ans_eg1
    assert w.int2braille(eg2) == ans_eg2
    assert w.int2braille(eg3) == ans_eg3


def test_Writer_braill2binary_str():
    eg1 = braille_cell.BrailleCell([ True, False, False, False, False, False ])
    ans_eg1 = "100000"

    eg2 = braille_cell.BrailleCell([ False, False, True, False, True, True ])
    ans_eg2 = "001011"

    eg3 = braille_cell.BrailleCell([ False for i in range(6) ])
    ans_eg3 = "000000"

    w = write.Writer()
    assert w.braille2binary_str(eg1) == ans_eg1
    assert w.braille2binary_str(eg2) == ans_eg2
    assert w.braille2binary_str(eg3) == ans_eg3


def test_Writer_braille2int():
    eg1 = braille_cell.BrailleCell([ True, False, False, False, False, False ])
    ans_eg1 = 32

    eg2 = braille_cell.BrailleCell([ False, False, True, False, True, True ])
    ans_eg2 = 11

    eg3 = braille_cell.BrailleCell([ False for i in range(6) ])
    ans_eg3 = 0

    w = write.Writer()
    assert w.braille2binary_str(eg1) == ans_eg1
    assert w.braille2binary_str(eg2) == ans_eg2
    assert w.braille2binary_str(eg3) == ans_eg3


def test_Writer_braille2unicode():
    eg1 = braille_cell.BrailleCell([ True, False, False, False, False, False ])
    ans_eg1 = '⠁'

    eg2 = braille_cell.BrailleCell([ False, False, True, False, True, True ])
    ans_eg2 = '⠦' 

    eg3 = braille_cell.BrailleCell([ False for i in range(6) ])
    ans_eg3 = '⠀'

    w = write.Writer()
    assert w.braille2binary_str(eg1) == ans_eg1
    assert w.braille2binary_str(eg2) == ans_eg2
    assert w.braille2binary_str(eg3) == ans_eg3

