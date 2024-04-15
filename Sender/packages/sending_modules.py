import time
from datetime import datetime
from w1thermsensor import W1ThermSensor
import serial

# Create a loop that records date time and temperature and sends it through LoRa

rate_of_measurement = 30	# Record data every 30 seconds
sensor = W1ThermSensor()

# Configure the serial connection
ser = serial.Serial(
	port='/dev/ttyACM0',	# Replace this with the port the USB-TO-LoRa-HF is plugged into.
	baudrate=115200,	# Set the device baud rate
)

def record_temperature() -> str: return str(round(sensor.get_temperature(), 1))
def record_time() -> str: return datetime.now().strftime("%H:%M:%S")
def write_message() -> str: return "~" + record_temperature() + "," +  record_time()
def open_serial_port():
	if not ser.is_open:
		ser.open()
def close_serial_port(): ser.close()
def send_message(message): ser.write(message.encode())
def wait(rate_of_measurement): time.sleep(rate_of_measurement)

# Create a loop that records and transmits the probe data of the USB-TO-LoRa-HF
#while True:
#	temperature_message = str(round(sensor.get_temperature(), 1))
#	timestamp_message = datetime.now().strftime("%H:%M:%S") 
#	message = "~" + temperature_message + "," + timestamp_message
#	if not ser.is_open:	# Ensure the serial port is open
#		ser.open()

#	ser.write(message.encode()) # Send temperature
#	print("Sending {} over LoRa".format(message))
#	ser.close()

#	time.sleep(rate_of_measurement)	# Sleep until data needs to be sent again
