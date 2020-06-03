"""
This is the Reader class, which is responsible for directly interfacing
with the Liblouis library functions.

This class allows for the program to output Braille from English,
and to turn input Braille into English to be interpreted by the wider
program or to store in a text file.
"""
from louis import translateString, backTranslateString
"""
Some possible tables:
    en-GB-g2.ctb  <-- Issues with 8-dot cells being generated
    en-gb-g1.utb
    en-us-g1.ctb
    en-us-g2.ctb
    en_GB.tbl
    en-ueb-g2.ctb <-- Unified English Braille

    More at:
        https://github.com/liblouis/liblouis/tree/master/tables
    or
        .../LibLouis/liblouis-3.12.0/tables/
"""


class Reader:


    @staticmethod
    def back_translate_item(in_str, t_tables=['unicode.dis', 'en-ueb-g2.ctb']):
        """Translates a string from braille into unicode English
        """
        result = backTranslateString(t_tables, in_str)
        return(result)


    @staticmethod
    def translate_item(in_str, t_tables=['unicode.dis', 'en-ueb-g2.ctb']):
        """Translates a string from unicode English into braille
        """
        result = translateString(t_tables, in_str)
        return(result)

