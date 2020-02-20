

class ViewBraille:

    
    def __init__(self, braille_pins=None):
        # TODO encapsulate all these variables in another class (BraillePins)
        self.br_in = [ i for i in range(0, 6) ]
        self.br_out = [ i for i in range(10, 16) ]
        self.br_in_space = 7
        self.enter = 30
        self.prev = 31
        self.next = 32
        # TODO prevent overlapping values for all the above variables
        self.disp_speed_delay = 500
        if braille_pins:
            self.br_in = braille_pins.br_in
            self.br_out = braille_pins.br_out
            self.br_in_space = braille_pins.br_in_space
            self.enter = braille_pins.enter
            self.prev = braille_pins.prev
            self.next = braille_pins.next
            self.disp_speed_delay = braille_pins.disp_speed_delay

    def _whitespace_macro(in_ws=None):
        """Modulate a 'whitespace' pause length depending on the type of
        whitespace it is supposed to be representing.
        """
        if in_ws == ' ':
            delay = 1
        elif in_ws == '\t':
            delay = 1.5
        elif in_ws == '\n':
            delay = 2
        elif in_ws is None:
            delay = 0.25
        else:
            delay = 1
        return(delay * self.disp_speed_delay)

    def str_print(in_str):
        pass

    def str_input(inputter):
        pass

""" TODO:
- Add callbacks for prev, next, and disp_speed
- Create mini loop to chain characters with delays and a mini-None-delay
"""
