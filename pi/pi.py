from functools import partial

from gpiozero import Button

# https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
braille_pins = [ 2, 3, 4, 17, 27, 22 ]

enter_pin = 18

# https://gpiozero.readthedocs.io/en/stable/recipes.html#button
braillers = [ Button(p) for p in braille_pins ]

braille_state = [ False * 6 ]


def update_dot_state(cell):
    braille_state[cell] = not braille_state[cell]


for n, i in enumerate(braillers):
    i.when_pressed = partial(update_dot_state, cell=n)

