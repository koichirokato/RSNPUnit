#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RSNPUnitConnector.py
 @brief ModuleDescription
 @date $Date$


"""
import serial
import socket
import json

import OpenRTM_aist
import RTC
import sys
import time
sys.path.append(".")

# Import RTM module


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
rsnpunitconnector_spec = ["implementation_id", "RSNPUnitConnector",
                          "type_name",         "RSNPUnitConnector",
                          "description",       "ModuleDescription",
                          "version",           "1.0.0",
                          "vendor",            "S.Okano",
                          "category",          "Category",
                          "activity_type",     "STATIC",
                          "max_instance",      "1",
                          "language",          "Python",
                          "lang_type", "SCRIPT",

                          "conf.default.IPaddress", "localhost",
                          "conf.default.SocketPort", "8000",
                          "conf.default.SerialPort", "10",
                          "conf.default.baudrate", "9600",
                          "conf.default.SocketOrSerial", "Socket",

                          "conf.__widget__.IPaddress", "text",
                          "conf.__widget__.SocketPort", "text",
                          "conf.__widget__.SerialPort", "text",
                          "conf.__widget__.baudrate", "text",
                          "conf.__widget__.SocketOrSerial", "radio",

                          "conf.__type__.IPaddress", "string",
                          "conf.__type__.SocketPort", "int",
                          "conf.__type__.SerialPort", "int",
                          "conf.__type__.baudrate", "int",
                          "conf.__type__.SocketOrSerial", "string",
                          
		                  "conf.__constraints__.SocketOrSerial", "(Socket,Serial)",
                          

                          ""]
# </rtc-template>

##
# @class RSNPUnitConnector
# @brief ModuleDescription
#
#


class RSNPUnitConnector(OpenRTM_aist.DataFlowComponentBase):

    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_SampleDataIn = RTC.TimedString(RTC.Time(0, 0), "null")
        self._SampleDataInIn = OpenRTM_aist.InPort(
            "SampleDataIn", self._d_SampleDataIn)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
		 - Name:  IPaddress
		 - DefaultValue: localhost
		"""
        self._IPaddress = ['localhost']

        """
		 - Name:  SocketPort
		 - DefaultValue: 8000
		"""
        self._SocketPort = [8000]

        """
         - Name:  SerialPort
		 - DefaultValue: 10
        """
        self._SerialPort = [10]

        """
         - Name:  baudrate
		 - DefaultValue: 9600
        """
        self._baudrate = [9600]

        """
		
		 - Name:  SocketOrSerial
		 - DefaultValue: Socket
		"""
        self._SocketOrSerial = ["Socket"]
        #############要変更#############

        self._Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._Serial = serial.Serial()
        # </rtc-template>

    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("IPaddress", self._IPaddress, "localhost")
        self.bindParameter("SocketPort", self._SocketPort, 8000)
        self.bindParameter("SerialPort", self._SerialPort,10)
        self.bindParameter("baudrate", self._baudrate,9600)
        self.bindParameter("SocketOrSerial", self._SocketOrSerial,"Socket")

        self.addInPort("SampleDataIn", self._SampleDataInIn)

        return RTC.RTC_OK

    def onActivated(self, ec_id):
        print("RSNPUnitConnectorRTC activate")
        self._SocOrSer = str(self._SocketOrSerial[0])
        if(self._SocOrSer=="Socket"):
            print("now Socket mode")
            print("now connecting to RSNPUnit")
            self._Sock.connect((self._IPaddress[0], self._Port[0]))
            
        elif(self._SocOrSer=="Serial"):
            print("now Serial mode")
            print("now connecting to RSNPUnit")
            self._Serial.port = "COM"+ str(self._SerialPort[0])
            self._Serial.baudrate = self._baudrate[0]
            self._Serial.open()
        
        print("connecting success")
        # failした場合 error
        return RTC.RTC_OK

    def onDeactivated(self, ec_id):
        print("RSNPUnitConnectorRTC deactivate")
        print("now disconnect to RSNPUnit")
        if(self._SocOrSer=="Socket"):
            self._Sock.close()
        elif(self._SocOrSer=="Serial"):
            self._Serial.close()
        print("disconnect success")
        # failした場合 error
        return RTC.RTC_OK

    def onExecute(self, ec_id):
        
        if self._SampleDataInIn.isNew():
            read_data = self._SampleDataInIn.read()
            rcv_data_str = str(read_data)
            print("recieve data: " + rcv_data_str)  # to debug
            send_data_json = {"data": [
                {"ac_id": 1, "ac": "robot state", "re_id": 1, "re": rcv_data_str, "co": ""}]}
            # json format

            # 出来ればサービスポートで定義する
            send_data_str = json.dumps(send_data_json)

            if(self._SocOrSer == "Socket"):
                self._Sock.send(send_data_str)
                print("send data by socket: " + send_data_str)
            elif(self._SocOrSer == "Serial"):
                self._Serial.write(send_data_str)
                print("send data by serial: " + send_data_str)

            time.sleep(2)
        return RTC.RTC_OK


def RSNPUnitConnectorInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=rsnpunitconnector_spec)
    manager.registerFactory(profile,
                            RSNPUnitConnector,
                            OpenRTM_aist.Delete)


def MyModuleInit(manager):
    RSNPUnitConnectorInit(manager)

    # Create a component
    comp = manager.createComponent("RSNPUnitConnector")


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == "__main__":
    main()
