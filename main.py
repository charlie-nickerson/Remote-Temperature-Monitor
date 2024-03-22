import time
from datetime import datetime
from w1thermsensor import W1ThermSensor
import boto3

s3_client = boto3.client('s3')
sensor = W1ThermSensor()

rate_of_upload = 60
rate_of_measurement = 5
aws_bucket_name = "remotemonitor"
log_file_name = 'temp.log'
time_file_name = "last_written.log"

while True:
    with open(time_file_name, 'r') as time_file:
        prev_time_stamp = int(time_file.read())

    #if we haven't written to the timestamp file in the last minute, update the value in the timestamp file
    if int(time.time()) >= prev_time_stamp + rate_of_upload: 
        # upload log to s3 
        s3_client.upload_file(log_file_name, 
                              aws_bucket_name, 
                              "log_{}.txt".format(datetime.now().strftime("%Y-%m-%d")))
        # update timestamp file
        with open(time_file_name, 'w') as file:
            file.write("{}".format(int(time.time())))

    # update log with entry
    with open(log_file_name, 'a') as file:
        file.write("{}\t{} C\n".format(int(time.time()), round(sensor.get_temperature(), 1)))
    
    # wait a certain amount of seconds before running again
    time.sleep(rate_of_measurement)
