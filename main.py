
from packages import receiver_modules

# Configure the serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',  # Replace with your device's serial port
    baudrate=115200,        # Set to your device's baud rate
    timeout=10            # Timeout in seconds to wait for a message
)

def main():
    open_serial_port()

    if headers_dont_exist():add_headers()
             
    while True:
            if its_time_to_upload():
                upload_log_to_aws()
                replace_the_date()
                initialize_log()

            message = received_message(ser)
            print("Receieved message {}".format(message))
            if is_formatted_correctly(message):
                print("Appending {} to log".format(message[1:])) 
                append_data_to_log(message)            
            else: print("Message was received in an incorrect format!")

if __name__ == "__main__":
    main()