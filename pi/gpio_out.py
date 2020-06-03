"""
This is a test file to ensure that the pins being used on the
Raspberry Pi are operational.
"""
from gpiozero import LED
from time import sleep

a = LED(18)
b = LED(23)
c = LED(24)
d = LED(25)
e = LED(12)
f = LED(16)

while True:
	a.on()
	sleep(1)
	b.on()
	sleep(1)
	c.on()
	sleep(1)
	d.on()
	sleep(1)
	e.on()
	sleep(1)
	f.on()
	sleep(1)
	a.off()
	sleep(1)
	b.off()
	sleep(1)
	c.off()
	sleep(1)
	d.off()
	sleep(1)
	e.off()
	sleep(1)
	f.off()
	sleep(1)
