import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Set pin numbering mode to BCM
led_pin = 18  # Use GPIO pin 18 (BCM numbering)
GPIO.setup(led_pin, GPIO.OUT)  # Set GPIO pin 18 as an output

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED is ON")  # Print message when LED is turned on
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        print("LED is OFF")  # Print message when LED is turned off
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up")  # Message for program termination and cleanup
