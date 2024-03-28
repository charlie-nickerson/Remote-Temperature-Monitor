import serial

# Configure the serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',  # Replace with your device's serial port
    baudrate=115200,        # Set to your device's baud rate
    timeout=10            # Timeout in seconds to wait for a message
)

# Ensure the serial port is open
if not ser.is_open:
    ser.open()

print("Waiting for message...")

# Wait for a message
while True:
    if ser.in_waiting > 0:
        incoming_bytes = ser.read(ser.in_waiting)
        print("Received bytes:", bytearray.fromhex(incoming_bytes.hex()).decode())  # Converts hex to ascii and prints the result

# Clean up
ser.close()