import serial

# Specify the port name and the baud rate. Adjust the baud rate as needed.
serial_port = '/dev/ttyACM0'
baud_rate = 9600  # This is a common baud rate, but check your device specs.

try:
    # Open serial connection
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        print("Serial port opened: ", ser.name)
        
        # Example: send a command to the LoRa device
        ser.write(b'Hello LoRa\n')  # The command needs to be in bytes
        
        # Wait for a response and read it
        response = ser.readline()
        print("Received response: ", response.decode())
        
except serial.SerialException as e:
    print("Error opening serial port: ", e)