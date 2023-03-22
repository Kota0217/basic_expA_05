#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from time import sleep

rospy.init_node('square_move')
sleep(1) #processing time

publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

msg = Twist()
sleep(2)

#move 1
msg.linear.x = 0.1 #0.1 m/s
msg.angular.z = 0.0 # 0.0 radian/s
publisher.publish(msg)
sleep(3)

#rotate 1
msg.linear.x = 0.0
msg.angular.z = math.pi/2 #rotate 90 degrees/s
publisher.publish(msg)
sleep(1)

#move 2
msg.linear.x = 0.1 #0.1 m/s
msg.angular.z = 0.0 # 0.0 radian/s
publisher.publish(msg)
sleep(3)

#rotate 2
msg.linear.x = 0.0
msg.angular.z = math.pi/2 #rotate 90 degrees/s
publisher.publish(msg)
sleep(1)

#move 3
msg.linear.x = 0.1 #0.1 m/s
msg.angular.z = 0.0 # 0.0 radian/s
publisher.publish(msg)
sleep(3)

#rotate 3
msg.linear.x = 0.0
msg.angular.z = math.pi/2 #rotate 90 degrees/s
publisher.publish(msg)
sleep(1)

#move 4
msg.linear.x = 0.1 #0.1 m/s
msg.angular.z = 0.0 # 0.0 radian/s
publisher.publish(msg)
sleep(3)


#stop
msg.linear.x = 0.0
msg.angular.z = 0.0 #stop moving
publisher.publish(msg)
