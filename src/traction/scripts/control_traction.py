#!/usr/bin/env python
# coding:utf-8

import rospy
#joy發送的message格式
from sensor_msgs.msg import Joy
#烏龜接收的message格式
from geometry_msgs.msg import Twist


def callback(data):
    twist=Twist()
    val1 = data.buttons[6]
    val2 = data.buttons[7]
    
    #輸入x時停止
    # if (data.buttons[2]==1):
    #     twist.linear.x = 0
    #     twist.angular.z =0

    print('Value1 : ' + str(val1) + '   |   ' +'Value2 : ' + str(val2))
    pub.publish(twist)

def FromJoyToTurtle():
    #callback函式也要用到所以宣告為global
    global pub

    pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
    sub = rospy.Subscriber('joy',Joy ,callback)
    
    rospy.init_node('ChangeJoyToTurtle',anonymous=True)
    rospy.spin()


if __name__ == '__main__':
    FromJoyToTurtle()