#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
from time import sleep
import numpy

box_dist = 0
min_index = 0
mode = 0
flag = 0
box_dist_init = 0

def callback(msg):
    global mode
    global flag
    global box_dist_init

    box_dist = msg.ranges[360]
    dist_edge = msg.ranges[719]

    #mode 0 : move forward to box and turn right
    if mode == 0 :
        if flag == 0 :
            box_dist_init = msg.ranges[360]
            flag = 1
        move.linear.x = 0.1
        pub.publish(move)
        if box_dist <= 0.6 : #stop position
            move.linear.x = 0.0  #stop running
            pub.publish(move)
            mode = 1 #mode 1
            # rotate 90 degrees right
            move.angular.z = - math.pi/6
            pub.publish(move)
            print 'rotate 90 degrees' 
            sleep(3.1)
            move.angular.z = 0.0
            pub.publish(move)


    #mode 1 : go straight and turn left
    if mode == 1 :
        print dist_edge
        move.linear.x = 0.1
        pub.publish(move)
        if dist_edge == float('inf') :
            move.linear.x = 0.1
            pub.publish(move)
            sleep(13)
            # rotate 90 degrees left
            move.angular.z = math.pi/6
            move.linear.x = 0.0
            pub.publish(move)
            print 'rotate 90 degrees 2'
            sleep(3.2)
            move.angular.z = 0.0
            pub.publish(move)
            mode = 2
    
    #mode 2 : go straight and turn left
    if mode == 2 :
        move.linear.x = 0.1
        if dist_edge == float('inf') :
            move.linear.x = 0.1
            pub.publish(move)
            sleep(20)
            # rotate 90 degrees left
            move.angular.z = math.pi/6
            move.linear.x = 0.0
            pub.publish(move)
            print 'rotate 90 degrees 3'
            sleep(3.1)
            move.angular.z = 0.0
            pub.publish(move)
            mode = 3


    #mode 3 : go straight and turn left
    if mode == 3 :
        move.linear.x = 0.1
        if dist_edge != float('inf') :
            move.linear.x = 0.1
            pub.publish(move)
            sleep(13)
            # rotate 90 degrees left
            move.angular.z = math.pi/6
            move.linear.x = 0.0
            pub.publish(move)
            print 'rotate 90 degrees 4'
            sleep(3.1)
            move.angular.z = 0.0
            pub.publish(move)
            mode = 4

    #mode 4 : back
    if mode == 4 :
        move.linear.x = -0.1
        pub.publish(move)
        #print 'rotate 90 degrees 5' 
        if msg.ranges[360] >= box_dist_init : 
            move.linear.x = 0.0
            pub.publish(move)
            mode = 5

    #mode 5 : 
    if mode == 5 : 
        print 'stop control'
        move.linear.x = 0.0
        move.angular.z = 0.0
        pub.publish(move)



rospy.init_node('side_of_box')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback) #define subscribe
pub = rospy.Publisher('/cmd_vel', Twist) #define publish

move = Twist()

rospy.spin() #wait until node update

