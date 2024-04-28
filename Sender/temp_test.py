import time
from w1thermsensor import W1ThermSensor
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the SSD1306 module.
import adafruit_ssd1306
# Import the RFM9x radio module.
import adafruit_rfm9x

sensor = W1ThermSensor()

# Button A
btnA = DigitalInOut(board.D5)
btnA.direction = Direction.INPUT
btnA.pull = Pull.UP

# Button B
btnB = DigitalInOut(board.D6)
btnB.direction = Direction.INPUT
btnB.pull = Pull.UP

# Button C
btnC = DigitalInOut(board.D12)
btnC.direction = Direction.INPUT
btnC.pull = Pull.UP

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# 128x32 OLED Display
reset_pin = DigitalInOut(board.D4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
# Clear the display.
display.fill(0)
display.show()
width = display.width
height = display.height

# Configure RFM9x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

while True:
    # Clear the image
    display.fill(0)
    temperature = str(sensor.get_temperature())
    # Check buttons
    if not btnA.value:
        # Button A Pressed
        display.text(temperature, width-85, height-7, 1)
        display.show()
        time.sleep(0.1)
    if not btnB.value:
        # Button B Pressed
        display.text(temperature, width-75, height-7, 1)
        display.show()
        time.sleep(0.1)
    if not btnC.value:
        # Button C Pressed
        display.text(temperature, width-65, height-7, 1)
        display.show()
        time.sleep(0.1)
