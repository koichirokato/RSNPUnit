#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import socket
import time
import configparser
import json

def main():

    # setting of configparser object
    config = configparser.ConfigParser()

    # reading parameter of Config.ini
    IPaddress = config['Settings']['IPaddress']
    Port = config['settings']['Port']

    # setting of socket object
    Socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # setting of IPaddress and Port
    Socket_client.connect((IPaddress, Port))

    # inicialize result data
    result_data = "null"

    # setting of json format data to send RSNPUnit
    send_sample_data_dict = {"data": [{"ac_id": "1", "ac": "robot1_state1", "re_id": "1", "re": result_data, "co": ""}]}

    # trans dict data (json format) to str data
    send_sample_data_str = json.dumps(send_sample_data_dict)

    while True:

        time.sleep(2)  #2s interval
        
        # send data to RSNPUnit by Socket communication
        Socket_client.send(send_sample_data_str)

        print(send_sample_data_str)


if __name__ == "__main__":
    main()
        
    
