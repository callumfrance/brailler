from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button, LED
from time import sleep

led = LED(17)
button = Button(16)
led.source = button


print(led.value)

btn_pin = Device.pin_factory.pin(16)

btn_pin.drive_low()
sleep(0.1)
print(led.value)

btn_pin.drive_high()
sleep(0.1)
print(led.value)
