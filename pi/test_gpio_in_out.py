import gpiozero

pinout = [18, 23, 24, 25, 12, 16]
pinin = [2, 3, 4, 17, 27, 22]
p_out = [ gpiozero.LED(p) for p in pinout ]
p_in = [ gpiozero.Button(p) for p in pinin ]

for i in p_in:
    i.bounce_time = 0.25

while True:
    for i in p_out:
        i.off()

    for n, i in enumerate(p_in):
       p_in[n].when_pressed = p_out[n].toggle 
