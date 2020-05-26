#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RSNPUnitConnector.py
 @brief ModuleDescription
 @date $Date$


"""

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
                          "conf.default.Port", "8000",

                          "conf.__widget__.IPaddress", "text",
                          "conf.__widget__.Port", "text",

                          "conf.__type__.IPaddress", "string",
                          "conf.__type__.Port", "int",

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
		 - Name:  Port
		 - DefaultValue: 8000
		"""
        self._Port = [8000]

        self._Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # </rtc-template>

    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("IPaddress", self._IPaddress, "localhost")
        self.bindParameter("Port", self._Port, 8000)

        # Set InPort buffers
        self.addInPort("SampleDataIn", self._SampleDataInIn)

        # Set OutPort buffers

        # Set service provider to Ports

        # Set service consumers to Ports

        # Set CORBA Service Ports

        return RTC.RTC_OK

    def onActivated(self, ec_id):
        print("activate")
        print("now connecting to RSNPUnit")
        self._Sock.connect((self._IPaddress[0], self._Port[0]))
        print("connecting success")
        return RTC.RTC_OK

    def onDeactivated(self, ec_id):
        print("deactivate")
        print("now disconnect to RSNPUnit")
        self._Sock.close()
        print("disconnect success")
        return RTC.RTC_OK

    def onExecute(self, ec_id):

        if self._SampleDataInIn.isNew():
            self._d_SampleDataIn = self._SampleDataInIn.read()
            rcv_data_str = str(self._d_SampleDataIn.data)
            print("recieve data: " + rcv_data_str)  # to debug
            #send_data_json = {"data": [
            #    {"ac_id": 1, "ac": "robot state", "re_id": 1, "re": rcv_data_str, "co": ""}]}
            #send_data_str = json.dumps(send_data_json)

            self._Sock.send(rcv_data_str)
            print("send data by socket: " + rcv_data_str)
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
