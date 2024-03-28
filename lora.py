import serial
import time

# Configure the serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',  # Replace with your device's serial port
    baudrate=115200,        # Set to your device's baud rate
)

# Ensure the serial port is open
if not ser.is_open:
    ser.open()

# The message to send
message = 'Hi'

# Send the message
ser.write(message.encode())

# Clean up
ser.close()
