import pytest

import brailler.reader.read as read


@pytest.fixture
def reader_1():
    return read.Reader()


def test_Reader_default(reader_1):
    assert isinstance(reader_1, read.Reader) == True


def test_Reader_get_input(reader_1):
    pass


def test_Reader_translate_item(reader_1):
    t_tables = ['unicode.dis', 'en-GB-g2.ctb']

    eg1 = "This is a test string"
    # eg2 = " "

    assert reader_1.translate_item(eg1, t_tables) == "⠠⠹⠀⠊⠎⠀⠁⠀⠞⠑⠌⠀⠌⠗⠬"
    # assert reader_1.translate_item(eg2, t_tables) == " "


def test_Reader_back_translate_item(reader_1):
    eg1 = "⠠⠹⠀⠊⠎⠀⠁⠀⠞⠑⠌⠀⠌⠗⠬"

    eg2 = " "

    assert reader_1.back_translate_item(eg1) == "This is a test string"
    assert reader_1.back_translate_item(eg2) == " "
