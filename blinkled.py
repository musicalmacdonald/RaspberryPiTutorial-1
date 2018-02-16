from gpiozero import LED
from time import sleep

def blink_led_once( blink_frequency, port ):
    """turns the led on for 1/2 the time specified in blink_frequency, then it off for the same amount of time."""
    myLED=LED(port)

    myLED.on()
    sleep(blink_frequency /2)
    myLED.off()
    sleep(blink_frequency /2 )

def blink_led_forever():
    """blink the led once per second in a never ending loop"""
    while True:
        blink_led_once(1)

def race_led():
    #led 1
    blink_led_once(2, 18)
    #led 2
    blink_led_once(2, 23)
    #led 3
    blink_led_once(2, 25)
    #led 4
    blink_led_once(2, 12)
    #led 5
    blink_led_once(2, 16)
    #led 6
    blink_led_once(2, 20)
    #led 7
    blink_led_once(2, 21)
    #led 8
    blink_led_once(2, 26)
    #led 9
    blink_led_once(2, 19)
    #led 10
    blink_led_once(2, 13)

if __name__ == "__main__":
    print("This will make the LED blink once")
    blink_led_once(2, 18)
