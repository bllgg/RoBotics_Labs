#!/usr/bin/env python2

from __future__ import print_function

import sys
import tf
import rospy
from lab_2_3dPose.srv import *

def euler_to_quarternion_client(a, b, c, format):
    rospy.wait_for_service('euler_to_quarternion')

    try:
        convert = rospy.ServiceProxy('euler_to_quarternion', angles)
        resp1 = convert(a, b, c, format)
        return [resp1.qx, resp1.qy, resp1.qz, resp1.qw]

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":

    # a = 0
    # b = 0
    # c = 0
    # format = "xyz"

    ####################################################################################################
    data = [[0.00, 0.00, 0.00, "xyz"],
            [1.57, 1.57, 1.57, "xyz"],

            [1.57, 0.00, 0.00, "xyz"],
            [0.00, 1.57, 0.00, "xyz"],
            [0.00, 0.00, 1.57, "xyz"],

            [3.14, 0.00, 0.00, "xyz"],
            [0.00, 3.14, 0.00, "xyz"],
            [0.00, 0.00, 3.14, "xyz"],

            [-1.57, 0.00, 0.00, "xyz"],
            [0.00, -1.57, 0.00, "xyz"],
            [0.00, 0.00, -1.57, "xyz"],

            [1.57, 1.57, 0.00, "xyz"],
            [1.57, 0.00, 1.57, "xyz"],
            [0.00, 1.57, 1.57, "xyz"],

            [1.57, 1.57, 0.00, "yxz"],
            [1.57, 0.00, 1.57, "yxz"],
            [0.00, 1.57, 1.57, "yxz"],

            [1.57, 1.57, 0.00, "zyx"],
            [1.57, 0.00, 1.57, "zyx"],
            [0.00, 1.57, 1.57, "zyx"]]

    for data_raw in data:
        a = data_raw[0]
        b = data_raw[1]
        c = data_raw[2]
        format = data_raw[3]
        print("Requesting %s, %s, %s, %s" %(a, b, c, format))

        result = euler_to_quarternion_client(a, b, c, format)

        print("Result %s, %s, %s, %s " %(result[0], result[1], result[2], result[3]))

    ####################################################################################################

    # print("Requesting %s, %s, %s, %s" %(a, b, c, format))

    # result = euler_to_quarternion_client(a, b, c, format)

    # print("Result %s, %s, %s, %s " %(result[0], result[1], result[2], result[3]))