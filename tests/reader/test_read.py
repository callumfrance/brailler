import pytest

import brailler.reader.read as read


@pytest.fixture
def reader_1():
    return read.Reader()


def test_Reader_default(reader_1):
    assert isinstance(r, reader_1) == True


def test_Reader_get_input(reader_1):
    pass


def test_Reader_translate_item(reader_1):
    eg1 = "This is a test string"
    eg2 = " "

    assert reader1.translate_item(eg1) == ""
    assert reader1.translate_item(eg2) == " "


def test_Reader_back_translate_item(reader_1):
    eg1 = ""
    eg2 = " "

    assert reader1.back_translate_item(eg1) == ""
    assert reader1.back_translate_item(eg2) == " "
