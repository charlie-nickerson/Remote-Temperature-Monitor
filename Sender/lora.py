import serial
import time



def send_message(message)
	# Configure the serial connection
	ser = serial.Serial(
	    port='/dev/ttyACM0',  # Replace with your device's serial port
	    baudrate=115200,        # Set to your device's baud rate
	)

	# Ensure the serial port is open
	if not ser.is_open:
	    ser.open()

	# Send the message
	ser.write(message.encode())

	# Clean up
	ser.close()
