import gpiozero
from time import sleep

import reader.read as read
import writer.write as write
from writer.braille_cell import BrailleCell

###################################################
## For testing code on a non raspberry pi device ##
# from gpiozero.pins.mock import MockFactory

# gpiozero.Device.pin_factory = MockFactory()
###################################################


class ViewBraille:

    
    def __init__(self, braille_pins=None):
        # TODO encapsulate all these variables in another class (BraillePins)
        self.br_in_pins = [ 2, 3, 4, 17, 27, 22 ]
        self.br_out_pins = [ 18, 23, 24, 25, 12, 16 ]
        self.in_enter_pin = 6
        self.prev_pin= 13
        self.next_pin = 19
        self.br_in = [ gpiozero.Button(p, bounce_time=0.1) for p in self.br_in_pins ]
        self.br_out = [ gpiozero.LED(p) for p in self.br_out_pins ]
        self.in_enter = gpiozero.Button(self.in_enter_pin, bounce_time=0.1)
        self.prev = gpiozero.Button(self.prev_pin, bounce_time=0.1)
        self.next = gpiozero.Button(self.next_pin, bounce_time=0.1)
        # TODO prevent overlapping values for all the above variables
        self.disp_speed_delay = 0.5 # "1 second"
        if braille_pins:
            self.br_in = braille_pins.br_in
            self.br_out = braille_pins.br_out
            self.br_in_space = braille_pins.br_in_space
            self.in_enter = braille_pins.in_enter
            self.prev = braille_pins.prev
            self.next = braille_pins.next
            self.disp_speed_delay = braille_pins.disp_speed_delay

    def _whitespace_macro(self, in_ws=None):
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
            delay = 0.5
        else:
            delay = 1
        sleep(delay * self.disp_speed_delay * 1.0)

    def b_char_print(self, in_b_char):
        """Prints a single braille character through the brailler device

          - turn on all keys OR whitespace
          - delay
          - turn off all keys
        """
        isBlank = True
        
        in_b_char = write.Writer.unicode2braille(in_b_char)

        for n, i in enumerate(in_b_char.cell):
            if i:
                self.br_out[n].on()
                isBlank = False

        if isBlank:
            self._whitespace_macro(i)

        self._whitespace_macro(None)

        for n, j in enumerate(range(6)):
            self.br_out[n].off()

        self._whitespace_macro(None)


    def str_print(self, in_str, ender="\n"):
        """Gets an input alphabetical string, converts to braille, and then
        parses through the braille char printer

        Callbacks may be triggered whilst this runs.

          - Convert incoming string into Grade 2 Braille
          - Iteratively print each character
        """
        print(in_str)
        in_b_str = read.Reader.translate_item(in_str)
        for i in in_b_str:
            self.b_char_print(i)

    def str_input(self, inputter):
        cells = list() # The cumulative inputted Braille characters from user
        cellString = '' # The string unicode representation of inputted Braille
        # b_in = list() # The six button values
        b_in = [False, False, False, False, False, False]
        notBreakout = True

        def reset_button_values():
            nonlocal b_in
            b_in = [False, False, False, False, False, False]

        reset_button_values() # Initialise the buttons to all be False
        
        print("\nBegin writing\n")

        # Mini functions to update the button readings when pressed by user
        def toggle0():
            b_in[0] = not b_in[0]
            print(b_in)
        def toggle1():
            b_in[1] = not b_in[1]
            print(b_in)
        def toggle2():
            b_in[2] = not b_in[2]
            print(b_in)
        def toggle3():
            b_in[3] = not b_in[3]
            print(b_in)
        def toggle4():
            b_in[4] = not b_in[4]
            print(b_in)
        def toggle5():
            b_in[5] = not b_in[5]
            print(b_in)

        # Function to capture cell information and append to the cell input list
        def char_input():
            nonlocal notBreakout
            """Note that this may need to be altered because two sequential
            spaces can indicate the start of a paragraph.
            """
            print("\nEnter pressed")
            if len(cells) > 1:
                    print("Last cell isBlank: ", str(cells[-1].isBlank))
                    if cells[-1].isBlank: # Last entered cell was blank -> check breakout
                        if BrailleCell(b_in).isBlank: # Two consecutive blanks -> break
                            print("Two consecutive isBlanks found")
                            notBreakout = False
                            return(None)
            # Now established that we need to keep writing cells
            x = BrailleCell(b_in)
            if x.isFull: # Interpret a full cell as a strikethrough - delete prev
                print("\nStrikethrough found")
                if len(cells) > 1:
                        cells.pop(-1)
            else:
                cells.append(x)
            # Flush button values
            reset_button_values()

        # Turn on the button behaviour now that we are reading user input
        self.br_in[0].when_pressed = toggle0
        self.br_in[1].when_pressed = toggle1
        self.br_in[2].when_pressed = toggle2
        self.br_in[3].when_pressed = toggle3
        self.br_in[4].when_pressed = toggle4
        self.br_in[5].when_pressed = toggle5
        self.in_enter.when_pressed = char_input

        # Loop to capture the user's entire input until they write a breakout
        while notBreakout:
            pass # This is an intentional pass statement

        # Turn off the button behaviour now that reading has completed
        for i in range(6):
            self.br_in[i].when_pressed = None
        self.in_enter.when_pressed = None

        # Get unicode of each BrailleCell in cells and squash into one string
        for i in cells:
            cellString += i.braille2unicode()

        # Back_translate captured chars into English
        output = read.Reader.back_translate_item(cellString)

        # Return back_translated string
        return(output)

    def option_select(self, in_options):
        self.str_print("")
        for n, i in enumerate(in_options):
            self.str_print(str(n) + " : " + i)
        try:
            ans = int(self.str_input("\n> "))
        except ValueError:
            ans = None

        if ans < 0 or ans > len(in_options):
            ans = None

        return(ans)

""" TODO:
- Add callbacks for prev, next, and disp_speed
"""
