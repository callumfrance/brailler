

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

    def b_char_print(in_b_char):
        """Prints a single braille character through the brailler device

          - turn on all keys OR whitespace
          - delay
          - turn off all keys
        """
        isBlank = True

        for i in in_b_char:
            if i:
                # self.br_out[i].on()
                isBlank = False

        if isBlank:
            self._whitespace_macro(in_ws)

        self._whitespace_macro(None)

        for j in range(6):
            # self.br_out[i].off()
            pass

    def str_print(in_str):
        """Gets an input alphabetical string, converts to braille, and then
        parses through the braille char printer

        Callbacks may be triggered whilst this runs.

          - Convert incoming string into Grade 2 Braille
          - Iteratively print each character
        """
        # in_b_str = in_str.toBraille()
        in_b_str = ''
        for i in in_b_str:
            curr = ""
            self.b_char_print(i)

    def str_input(inputter):
        notEntered = False
        b_in = [ False for i in range(6) ]
        while notEntered:
            for n, i in enumerate(self.br_in):
                # This probably wont work but event handler...
                i.when_pressed = lambda x: self.b_in[x] = not self.b_in[x]
            # TODO add means of pressing space and enter
            # TODO add means of terminating sequence (enter -> enter)
        # TODO add means of converting into a list of BrailleCells
        # TODO add way of converting all these BrailleCells into unicode
        # TODO add way of turning this unicode string into alphabetical
        # TODO return the alphabetical string
        return(None)

""" TODO:
- Add callbacks for prev, next, and disp_speed
- Create mini loop to chain characters with delays and a mini-None-delay
"""
