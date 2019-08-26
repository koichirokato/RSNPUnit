#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import serial
import time
import configparser
import json

def main():

    # setting of configparser object
    config = configparser.ConfigParser()

    # reading parameter of Config.ini
    Serial_port = config['Settings']['SerialPort']
    Serial_baudrate = config['settings']['baudrate']

    # setting of serial object
    Serial_obj = serial.Serial()

    # setting of serial communication
    Serial_obj.port = "COM" + str(Serial_port)
    Serial_obj.baudrate = Serial_baudrate

    # connecting to RSNPUnit
    Serial_obj.open()

    # inicialize result data
    result_data = "null"

    # setting of json format data to send RSNPUnit
    send_sample_data_dict = {"data": [
        {"ac_id": "1", "ac": "robot1_state1", "re_id": "1", "re": result_data, "co": ""}]}

    # trans dict data (json format) to str data
    send_sample_data_str = json.dumps(send_sample_data_dict)

    while True:
        time.sleep(2)  # 2s interval

        # send data to RSNPUnit by Serial communication
        Serial_obj.write(send_sample_data_str)

        #only print data
        print("send_data: "+ send_sample_data_str)

if __name__ == "__main__":
    main()
