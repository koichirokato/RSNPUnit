# coding:utf-8
#!/usr/bin/env python
import time
import socket
import sys
import threading
import csv
import datetime
import RPi.GPIO as GPIO

ID = '1'  # ラズパイID
SensorPin = 4  # ピン番号
count = 0  # カウントcount初期化0
GPIO.setmode(GPIO.BCM)  # GPIO設定
GPIO.setup(SensorPin, GPIO.IN)
PORT = 8000  # PORT番号設定
INTERVAL = 2 # 送信間隔


def main():
    
	sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	hostname = "127.0.1.1"#sock_client.gethostname
	sock_client.connect((hostname, PORT))

	print ("connection success")

	state = 0
    
	try:
		while True:

			sensor_val = GPIO.input(SensorPin)

			if sensor_val == 1 and state == 0:
				print ("switch ON")
				send_data = "{\"data\":[{\"ac_id\":1,\"ac\":\"sensor status\",\"re_id\":1,\"re\":\"on\",\"co\":\"\"}]}"
				print ("send data: "+ send_data)
				sock_client.send(send_data)
			else:
				print ("switch OFF")
				send_data = "{\"data\":[{\"ac_id\":1,\"ac\":\"sensor status\",\"re_id\":1,\"re\":\"off\",\"co\":\"\"}]}"
				print ("send data: "+ send_data)
				sock_client.send(send_data)

			time.sleep(INTERVAL)
			state == sensor_val
    
	except KeyboardInterrupt:
		print("finish")
		GPIO.cleanup()
		sock_client.close()

if __name__ == '__main__':
	main()
