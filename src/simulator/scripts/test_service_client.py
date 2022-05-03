#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from std_srvs.srv import *

# def control(req):
#     global data
#     if req.data:
#         send_control(req.data)
# 	    print("get request true")
#         data="up"
#         return SetBoolResponse(True,'get True signal')
#     else:
#         send_control(req.data)
# 	    print("get request false")
#         data='down'
#         return SetBoolResponse(False,'get False signal')

def Call_Service():
    try:
        # rospy.wait_for_service('clear')
        
        # ServiceProxy = rospy.ServiceProxy('clear', Empty  ,persistent=False, headers=None)
        # ServiceProxy()
        
        ServiceProxy = rospy.ServiceProxy('clear', Empty  ,persistent=False, headers=None)
        ServiceProxy()


        # traction = rospy.Service('push_rod_controller', SetBool, control)
        # traction()
        
        return print("Service call Success!")    

    except rospy.ServiceException as e:
        return print("Service call failed: %s"%e)

if __name__ == "__main__":
    Call_Service()
    print('End')