##import RPi.GPIO as GPIO

import decoder
import diode

##GPIO.setmode(GPIO.BCM)
##GPIO.setup(24, GPIO.OUT)

decrypter = decoder.Decoder()
LEDcontrol = diode.Diode()
LED_prev_on = False

message = "Hello world"
morse_msg = decrypter.decode_message(message)
LEDcontrol.set_message(morse_msg)

while True:
    LEDcontrol.update()
    LED_on = LEDcontrol.light_on
##    GPIO.output(24, LEDcontrol.LEDon)

    if LED_prev_on != LED_on:
        print('ON' if LED_on else 'OFF')

    LED_prev_on = LED_on
