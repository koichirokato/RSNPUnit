<h1>RSNP Unit English manual</h1>


- [1. Connect to the Unit](#1-connect-to-the-unit)
  - [1.1 Connect to the Unit and PC](#11-connect-to-the-unit-and-pc)
  - [1.2 Connect to the Unit](#12-connect-to-the-unit)
- [2. Set up the Unit](#2-set-up-the-unit)
  - [2.1 Connect to Wireless LAN](#21-connect-to-wireless-lan)
  - [2.2 Set up the file of RSNP properties](#22-set-up-the-file-of-rsnp-properties)
- [3. Run action of the RSNP Unit](#3-run-action-of-the-rsnp-unit)
  - [3.1 Execution of RSNP communication program](#31-execution-of-rsnp-communication-program)
  - [3.2 Program execution daemonized](#32-program-execution-daemonized)
  - [3.3 Connect to the Unit use ROS](#33-connect-to-the-unit-use-ros)
  - [3.4 Check the status](#34-check-the-status)
- [4 Data format of communication data to the Unit](#4-data-format-of-communication-data-to-the-unit)
## 1. Connect to the Unit  
### 1.1 Connect to the Unit and PC   
You can use LAN cable to connect to the Unit and PC.  
<img src="https://user-images.githubusercontent.com/44587055/63603092-d60eb380-c603-11e9-88ed-a2e9b6bb35d4.png" width=45%>  

### 1.2 Connect to the Unit
If you use linux, use ssh command.  
`~$ ssh pi@rsnpunit -p 22`  

If you can connect the Unit , the following screen is displayed.  
<img src="https://user-images.githubusercontent.com/44587055/63604122-ffc8da00-c605-11e9-9512-c9dffb785908.png" width=60%>  

## 2. Set up the Unit  
### 2.1 Connect to Wireless LAN  
You check your SSID and password. And, edit file wpa_supplicant.conf. use following command.  

`$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`  

※This time we use “nano” editor. Of course you use any editor.  
Please add as follows.  
```  
network={  
	ssid=”your SSID”  
	psk=”your password”  	
}  
```  

Next, you reset the wireless LAN.  
`~$ sudo ifdown wlan0`  
The wireless LAN will turn off after a few seconds, so enter the command as shown below and execute it.  
`~$ sudo ifup wlan0`  
You can check status of wireless LAN to use below command.  
`~$ ifconfig`  
If there is an enumeration of numbers in the `inet` line of the item` wlan0: `, it is connected.  

### 2.2 Set up the file of RSNP properties  
In desktop of RSNP Unit, there is derectory of RSNPUnit.And go to the `"Datalog"` directory.  
`~$ cd ~/RSNPUnit/DataLog/`  

Next, you enter following command.  
`~$ sudo nano Config.properties`  

The default is as follows, so change the ip address to raspberry pi's ip address     
~~~text
Configuretion
robot_id  = 1  
end_point = http://robots.aiit.ac.jp:8080/UpdateNotificationState/services
send_interval = 10000
ip_address = your RSNP Unit ip addres
port = 8000
~~~  

## 3. Run action of the RSNP Unit
Note that it is necessary to connect PC or device after starting the program on the RSNP Unit.  

### 3.1 Execution of RSNP communication program  
to go to derectory of RSNPUnit, enter command.  
`~$ cd ~/RSNPUnit/`  
And, run the program.  
`~$ java -jar RSNPNotifi.jar`  

### 3.2 Program execution daemonized   
In production


### 3.3 Connect to the Unit use ROS  
Use socket communication of python.  


### 3.4 Check the status  
You can check below URL.
Confirmation is complete if it is displayed on the browser as shown below.  
This time, it is just an example of displaying the operating status of RaspberryPi and the status of the sensor connected to it.  
The figure below shows an example of operating the robot with robot_id = 2.  
http://robots.aiit.ac.jp:8080/Robomech2019/  
<img src="https://user-images.githubusercontent.com/44587055/58847016-4caeab80-86bc-11e9-9b39-e87f95fe140a.png" width=60%>  


## 4 Data format of communication data to the Unit  
The transmission data is currently **character string data**. However, it is necessary to define it with the following five types of data.  

- **Action_id**
- **Action_name**  
- **Result_id**  
- **Result_data**  
- **comment**  

Here, the actual data format is the following json format. Within `{...}`, it begins with `["data":]`, and then within the array brackets (`[]`), one type of data enters one element of the array. You The specification name and value enclosed in double quotations (`" `) are separated by commas (`: `) .The corresponding data etc. are entered at 3 points (` ... `). Actually, please send the data on a single line, but note that if you send data with other specifications, the RSNP unit cannot receive it.  

~~~text
{  
  "data":  
  [  
    {  
      "ac_id": ... ,  
      "ac": ... ,  
      "re_id": ... ,  
      "re": ... ,  
      "co": ...  
    },  
    {...},  
    ...  
  ]  
}  
~~~  


Please note that the data names are abbreviated as shown in the table below.  
|     data name    | Abbreviation |
| :--------------: | :-------: |
|  **Action_id**   | **ac_id** |
|  **Action_name** |  **ac**   |
|  **Result_id**   | **re_id** |
| **Result_data**  |  **re**   |
|   **comment**    |  **co**   |