import gpiozero

###################################################
## For testing code on a non raspberry pi device ##
from gpiozero.pins.mock import MockFactory

gpiozero.Device.pin_factory = MockFactory()
###################################################


class ViewBraille:

    
    def __init__(self, braille_pins=None):
        # TODO encapsulate all these variables in another class (BraillePins)
        self.br_in_pins = [ 2, 3, 4, 17, 27, 22 ]
        self.br_out_pins = [ 18, 23, 24, 25, 12, 16 ]
        self.br_in_space_pin = 5
        self.in_enter_pin = 6
        self.prev_pin= 13
        self.next_pin = 19
        self.br_in = [ gpiozero.Button(p) for p in self.br_in_pins ]
        self.br_out = [ gpiozero.LED(p) for p in self.br_out_pins ]
        self.br_in_space = gpiozero.Button(self.br_in_space_pin)
        self.in_enter = gpiozero.Button(self.in_enter_pin)
        self.prev = gpiozero.Button(self.prev_pin)
        self.next = gpiozero.Button(self.next_pin)
        # TODO prevent overlapping values for all the above variables
        self.disp_speed_delay = 500
        if braille_pins:
            self.br_in = braille_pins.br_in
            self.br_out = braille_pins.br_out
            self.br_in_space = braille_pins.br_in_space
            self.in_enter = braille_pins.in_enter
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

    def str_input(self, inputter):
        b_in = [ False for i in range(6) ]
        notEntered = True
        enter_count = 0

        def toggle0():
            b_in[0] = not b_in[0]
        def toggle1():
            b_in[1] = not b_in[1]
        def toggle2():
            b_in[2] = not b_in[2]
        def toggle3():
            b_in[3] = not b_in[3]
        def toggle4():
            b_in[4] = not b_in[4]
        def toggle5():
            b_in[5] = not b_in[5]
        def inc_enter():
            """Determines if an enter is submitting a character, a space,
            or exiting

            This is all untested
            """
            spaceEntered = True
            if enter_count == 0:
                # TODO Save current b_in as a braille cell at this point
                for i in b_in: # Check if whitespace or actual char
                    if i is True:
                        spaceEntered = False
                        break
                if spaceEntered:
                    enter_count += 1
            else:
                for i in b_in: # Check if whitespace or actual char
                    if i is True:
                        spaceEntered = False
                        break
                if spaceEntered:
                    # Two spaces --> exit typing here
                    notEntered = False
            b_in = [ False for i in range(6) ]

        self.br_in[0].when_pressed = toggle0
        self.br_in[1].when_pressed = toggle1
        self.br_in[2].when_pressed = toggle2
        self.br_in[3].when_pressed = toggle3
        self.br_in[4].when_pressed = toggle4
        self.br_in[5].when_pressed = toggle5

        self.in_enter.when_pressed = inc_enter

        while notEntered:
            # wait for the pressing space and enter
            # wait for the terminating sequence (in_enter -> in_enter)
            pass
        # TODO add means of converting into a list of BrailleCells
        # TODO add way of converting all these BrailleCells into unicode
        # TODO add way of turning this unicode string into alphabetical
        # TODO return the alphabetical string
        return(None)

    def option_select(self, in_options):
        ViewBraille.str_print("")
        for n, i in enumerate(in_options):
            ViewBraille.str_print(str(n) + " : " + i)
        try:
            ans = int(ViewBraille.str_input(self, "\n> "))
        except ValueError:
            ans = None

        if ans < 0 or ans > len(in_options):
            ans = None

        return(ans)

""" TODO:
- Add callbacks for prev, next, and disp_speed
- Create mini loop to chain characters with delays and a mini-None-delay
"""
