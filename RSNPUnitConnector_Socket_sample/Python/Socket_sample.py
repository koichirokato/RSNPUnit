#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import socket
import time
import ConfigParser #for Python2
#import configparser #for Python3

def main():

    # setting of configparser object
    config = ConfigParser.ConfigParser() #for Python2
    # config = configparser.ConfigParser() #for Python3

    # read Config.ini
    config.read("./Config.ini")

    # reading parameter of Config.ini
    IPaddress = config.get('Settings','IPaddress')
    Port = config.get('Settings','Port')
    Port = int(Port)
    print("IPaddr = [{}] Port = [{}]".format(IPaddress, Port))

    # setting of socket object
    Socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # setting of IPaddress and Port
    Socket_client.connect((IPaddress, Port))

    # inicialize result data
    result_data = '"hoge"'
    count = 0
    # setting of json format data to send RSNPUnit
    #send_data = '{"data": [{"ac_id": "1", "ac": "robot_state", "re_id": "1", "re": '+result_data+', "co": ""},{"ac_id": "2", "ac": "robot_state", "re_id": "2", "re": '+result_data+', "co": ""}]}'

    while True:

        time.sleep(180)  #5s interval

        count += 1

        send_data = '{"data": [{"ac_id": "1", "ac": "robot_state", "re_id": "1", "re": '+result_data+', "co": ""},{"ac_id": "2", "ac": "robot_state", "re_id": "2", "re": '+str(count)+', "co": ""}]}'

        # send data to RSNPUnit by Socket communication
        Socket_client.send(send_data)

        #only print data
        print("send_data: " + send_data)


if __name__ == "__main__":
    main()