#!/usr/bin/env python

from __future__ import print_function

# from simulator.srv import AddTwoInts,AddTwoIntsResponse
import rospy

# def handle_add_two_ints(req):
    # print("Success")
    # return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('clear_node')
    s = rospy.Service('clear')
    # s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Clear Success!")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()