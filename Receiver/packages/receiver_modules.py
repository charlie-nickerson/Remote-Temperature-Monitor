import serial
import boto3
from datetime import datetime
import csv

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

aws_bucket_name = "remotemonitor"
log_file_name = 'templog.csv'
time_file_name = "last_written.log"
column_headings = ['Temperature', 'Time']

# Configure the serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',  # Replace with your device's serial port
    baudrate=115200,        # Set to your device's baud rate
    timeout=10            # Timeout in seconds to wait for a message
)

# Ensure the serial port is open
def open_serial_port():
    if not ser.is_open:
        ser.open()

def headers_dont_exist() -> bool:
    with open(log_file_name, 'r', newline='') as file:
            # Read the first line
            current_headings = file.readline().strip().split(',')
            
            # Check if the current headings match the expected headings
            if current_headings != column_headings:
                # The headings either don't exist or don't match
                file.close()
                return True
            else:
                file.close()
                return False

def is_formatted_correctly(message) -> bool:
     if (message[0] == '~'):
          return True
     else:
          return False
     
def add_headers():
    with open(log_file_name, mode='a', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)
        writer.writerow(['Temperature', 'Time'])
        file.close()
        return

def append_data_to_log(message):
     with open(log_file_name, mode='a', newline='') as file:
          writer = csv.writer(file, quoting=csv.QUOTE_NONE)
          writer.writerow([i.strip() for i in message[1:].split(',')])
          file.close()
          return
     
def received_message(ser) -> str:
     waiting = True
     print("Waiting for message...")
     while waiting:
        if ser.in_waiting > 0:
            return decoded_message(ser)
        
     

def decoded_message(encoded_message) -> str: return bytearray.fromhex(
               encoded_message.read(encoded_message.in_waiting).hex()).decode()

def its_time_to_upload() -> bool:
    with open(time_file_name, mode='r') as file:
        if file.readline() == datetime.now().strftime("%Y-%m-%d"):
            file.close()
            return False
        else:
             file.close()
             return True
    
def replace_the_date():
     print("Writing date")
     with open(time_file_name, mode='w') as file:
        file.write("{}".format(datetime.now().strftime("%Y-%m-%d")))
        file.close()

def upload_log_to_aws():
     s3.upload_file(log_file_name, 
                              aws_bucket_name, 
                              "log_{}.csv".format(datetime.now().strftime("%Y-%m-%d")))

def initialize_log():
    with open(log_file_name, 'w') as file:
        pass  # No need to write anything, just opening in 'w' mode truncates the file
    file.close()
    add_headers()




# open_serial_port()

# if headers_dont_exist():add_headers()
             
# while True:
#         if its_time_to_upload():
#              upload_log_to_aws()
#              replace_the_date()
#              initialize_log()

#         message = received_message(ser)
#         print("Receieved message {}".format(message))
#         if is_formatted_correctly(message):
#             print("Appending {} to log".format(message[1:])) 
#             append_data_to_log(message)            
#         else: print("Message was received in an incorrect format!")
        

# # Clean up
# ser.close()