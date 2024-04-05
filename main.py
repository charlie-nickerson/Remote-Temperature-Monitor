from packages.data_transmission_lora import *

rate_of_measurement = 30

while True:
	message = write_message()
	print("Sending {} over LoRa".format(message))
	open_serial_port()
	send_message(message)
	close_serial_port()
	wait(rate_of_measurement)
