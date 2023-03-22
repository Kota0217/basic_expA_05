#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
from time import sleep
import numpy

box_dist = 0
min_index = 0

def callback(msg):
    #reset lenear x
    move.linear.x = 0.0

    #print minimum of msg.ranges
    box_dist = min(msg.ranges)
    print box_dist
    min_index = msg.ranges.index(box_dist)
    print min_index
    degree = (min_index-360.0)/4.0
    print degree

    #rotate the robot to move towards the box
    #if robot turns to the box
    if  math.fabs(min_index-360) < 30:
        move.angular.z = 0.0  #stop running
        print 'stop rotation'
        pub.publish(move)
        print 'move forward'
        move.linear.x = 0.1
    elif box_dist == float('inf') :
        #rotate faster
        move.angular.z = 0.3
        print 'rotate faster'
    else :
        #rotate robot
        #box is left
        if numpy.sign(degree) == 1 :
            move.angular.z = 0.1
        else : #box is right
            move.angular.z = -0.1
    
    if box_dist <= 1.0: #stop position
        move.linear.x = 0.0  #stop running
        print 'stop control'

    pub.publish(move)

rospy.init_node('check_obstacle')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback) #define subscribe
pub = rospy.Publisher('/cmd_vel', Twist) #define publish

move = Twist()

rospy.spin() #wait until node update

