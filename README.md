# Remote Temperature Monitoring Device for Rivers and Streams (RTMD-RS)

## Project Overview
The Remote Temperature Monitoring Device for Water Streams (RTMD-RS) is an innovative solution designed to measure and log water temperature in streams. Utilizing LoRa technology for wireless data transmission, this device sends temperature data and timestamps to a central computer connected to the internet. The data is logged into a CSV file and automatically uploaded to an AWS S3 bucket daily. This project aims to facilitate remote environmental monitoring with an emphasis on affordability, simplicity, and accessibility.

## Proof of Concept:
![Device Outside](images/device_outside.jpg)

## Internal Components

![Device Inside](images/device_inside.jpg)

### Features
- Real-time water temperature monitoring with timestamp.
- Long-range data transmission via LoRa.
- Energy-efficient design powered by solar panels.
- Automated daily data upload to AWS S3 bucket.
- Detailed logging of temperature data in CSV format.

### Components
- Raspberry Pi Zero WH
- Waveshare USB to LoRa Data Transfer Module (SX1262-based)
- Solar Power Manager (B) with embedded 10000mAh Li-Po Battery
- 1W Mini Solar Panels (5V 6V)
- Raspberry Pi Zero 2 Case with micro USB to female USB adapter
- Gikfun DS18B20 Waterproof Digital Temperature Sensor
- Micro USB cable
- Female to Female Wires

Total Project Cost: Approximately $112.11

[Amazon Wishlist for Components](https://www.amazon.com/hz/wishlist/ls/2TMNA3738QL0E?ref_=wl_dp_view_your_list)

## Installation

### Hardware Setup
1. Assemble the Raspberry Pi Zero WH with the Raspberry Pi Zero 2 Case.
2. Connect the Gikfun DS18B20 Temperature Sensor to the Raspberry Pi using the Female to Female Wires.
3. Plug the Waveshare USB to LoRa Dongle into the Raspberry Pi via the USB adapter.
4. Connect the Solar Power Manager to the Raspberry Pi and the Mini Solar Panels for power supply.

### Software Setup

## AWS
- You will need to replace the bucket name with the name of your bucket in the receiver and sender modules and you will also need to configure the AWS CLI using the command `aws configure`. 

## Dependencies (Use pip3 install)
- pyserial
- boto3
- w1thermsensor
- datetime
- time
- awscli

## Usage
1. When installing the Waveshare USB to LoRa Data Transfer Module be sure to specify the serial port id in the receiver and sender modules under packages.
2. When using the Solar Power Manager (B) with embedded 10000mAh Li-Po Battery with the raspberry pi zero wh make sure to open the solar power manager and set the voltage output to 5 volts.
3. To edit the frequency at which data is recorded you can change the variable "rate_of_measurement" under the sender module.