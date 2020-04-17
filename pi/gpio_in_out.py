import gpiozero

pinout = [18, 23, 24, 25, 12, 16]
pinin = [2, 3, 4, 17, 27, 22]

p_out = [ gpiozero.LED(p) for p in pinout ]

p_in = [ gpiozero.Button(p, bounce_time=0.25) for p in pinin ]

for i in p_out:
        i.on()

for n, i in enumerate(p_in):
	p_in[n].when_pressed = p_out[n].toggle 

print("Setup completed\n")

while True:
	pass
