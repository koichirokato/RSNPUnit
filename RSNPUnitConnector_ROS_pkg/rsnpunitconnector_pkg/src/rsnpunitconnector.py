#! /usr/bin python
# -*- coding: utf-8 -*-

import rospy
import socket
import configparser
from rsnpunitconnector_pkg.msg import send_msg

def connection_config():
		# setting of configparser object
		config_par = configparser.ConfigParser()
    # read Config.ini
		config_par.read("config.ini")
		# reading parameter of Config.ini
		ipaddress = config_par.get('Settings','IPaddress')
		port = config_par.get('Settings','Port')
		port = int(port)

		return ipaddress, port

    # Instantiate send_message
		#ins_msg = send_msg()
		#msg_data = ins_msg.message_data

def ros_process():
		rospy.init_node('rsnpunitconnector', anonymous=True)
		rospy.Subscriber('connection_topic', send_msg, callback)
		rospy.spin()

def callback(msg):
		rospy.loginfo("msg: [%s]" % msg.message_data)
		sock.send(str(msg.message_data))

if __name__ == '__main__':
		# setting of socket object
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ipaddr, port = connection_config()
		#connecting by socket
		sock.connect((ipaddr, port))
    
		try:
			ros_process()
		except rospy.ROSInterruptException: pass

