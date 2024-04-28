import RPi.GPIO as GPIO
import time

# Set the GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin where the sensor is connected
SENSOR_PIN = 4
GPIO.setup(SENSOR_PIN, GPIO.IN)

def read_water_level():
    # Read the sensor input
    water_detected = GPIO.input(SENSOR_PIN)
    if water_detected:
        print("Water level detected!")
    else:
        print("No water level detected.")

try:
    while True:
        read_water_level()
        time.sleep(1)  # Delay for 1 second

except KeyboardInterrupt:
    print("Program stopped manually")

finally:
    GPIO.cleanup()  # Clean up all GPIO to ensure no conflicts

