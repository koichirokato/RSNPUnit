#! /usr/bin python
# -*- coding: utf-8 -*-

import rospy
from rsnpunitconnector_pkg.msg import send_msg

def publisher():

    # ROS setting
    rospy.init_node('sendnodesample', anonymous=True)

    pub = rospy.Publisher('connection_topic', send_msg, queue_size=50)
    
    rosrate = rospy.Rate(1) # 1[hz]

    count = 0
    
    while not rospy.is_shutdown():
			
	# Instantiate send_msg
        ins_msg = send_msg()

        result_data_str = str(count)
        time = rospy.get_time()
        time_str = str(time)
        json_data_1 = '{"data":[{"ac_id":"1","ac":"robot1_state1","re_id":"1","re":'+ result_data_str +',"co":"test"},{"ac_id":"2","ac":"robot1_state2","re_id":"2","re":'+ time_str +',"co":"test"}]}'

        rospy.loginfo(json_data_1)

        ins_msg.message_data = json_data_1

        pub.publish(ins_msg)
        count += 1
        rosrate.sleep()

if __name__ == '__main__':
        try:
            publisher()
        except rospy.ROSInterruptException: pass
