#!/usr/bin/env python
# coding:utf-8

import rospy
#joy發送的message格式
from sensor_msgs.msg import Joy
#烏龜接收的message格式
from geometry_msgs.msg import Twist


def callback(data):
    twist=Twist()
    twist.linear.x = data.axes[1]
    twist.angular.z = data.axes[0]
    
    # 輸入x時停止
    if (data.buttons[2]==1):
        twist.linear.x = 0
        twist.angular.z =0

    print('speed: %.2f, turn: %.2f'%(twist.linear.x,twist.angular.z))
    pub.publish(twist)

def FromJoyToTurtle():
    #callback函式也要用到所以宣告為global
    global pub

    pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
    sub = rospy.Subscriber('joy',Joy ,callback)
    
    rospy.init_node('PS4_Joystick_Control_turtlesim',anonymous=False)
    rospy.spin()


if __name__ == '__main__':
    FromJoyToTurtle()