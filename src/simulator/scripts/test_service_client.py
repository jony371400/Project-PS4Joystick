#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from std_srvs.srv import *

def Call_Service():
    try:
        rospy.wait_for_service('clear')
        ServiceProxy = rospy.ServiceProxy('clear', Empty)
        return print("Service call Success!")        
    except rospy.ServiceException as e:
        return print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    Call_Service()
    print('End')