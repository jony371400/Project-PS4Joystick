#!/usr/bin/env python

# import rospy
# from std_msgs.msg import String

import rospy
from geometry_msgs.msg import Twist

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    vel = Twist()
    
    while not rospy.is_shutdown():
        print('Traction Processs Start!')
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)

        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 35

        rospy.loginfo("Radius = %f",999)

        pub.publish(vel)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
