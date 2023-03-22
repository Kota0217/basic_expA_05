#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    print msg.ranges[360] #front view of turtlebot
    move.linear.x = 0.2
    if msg.ranges[360] <= 1.5: #stop position
        move.linear.x = 0.0  #stop running
    pub.publish(move)

rospy.init_node('check_obstacle')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback) #define subscribe
pub = rospy.Publisher('/cmd_vel', Twist) #define publish

move = Twist()

rospy.spin() #wait until node update

