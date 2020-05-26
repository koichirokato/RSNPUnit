#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file SampleSendTest.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

json_sample_data = '{"data": [{"ac_id": 1, "ac": "robot state", "re_id": 1, "re": "data", "co": ""}]}'

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
samplesendtest_spec = ["implementation_id", "SampleSendTest", 
		 "type_name",         "SampleSendTest", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "S.Okano", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.Data", json_sample_data,
		 "conf.__widget__.Data", "text",
		 "conf.__type__.Data", "string",
		 ""]
# </rtc-template>

##
# @class SampleSendTest
# @brief ModuleDescription
# 
# 
class SampleSendTest(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_send_json_str =  RTC.TimedString(RTC.Time(0, 0), "null")
		self._sendOut = OpenRTM_aist.OutPort("out", self._d_send_json_str)

		"""
		 - Name:  data
		 - DefaultValue: 
		"""
		self._Data = [json_sample_data]

	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		
		# Set OutPort buffers
		self.addOutPort("out",self._sendOut)

		self.bindParameter("Data", self._Data, json_sample_data)

		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	def onActivated(self, ec_id):
		print "on Activate"
		return RTC.RTC_OK

	def onDeactivated(self, ec_id):
		print "on Deactivate"
		return RTC.RTC_OK
	
	def onExecute(self, ec_id):

		time.sleep(1)
		self._d_send_json_str.data = self._Data[0]
		self._sendOut.write()
		print self._d_send_json_str
		
		return RTC.RTC_OK

def SampleSendTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=samplesendtest_spec)
    manager.registerFactory(profile,
                            SampleSendTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SampleSendTestInit(manager)

    # Create a component
    comp = manager.createComponent("SampleSendTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

