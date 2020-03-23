#!/usr/bin/env python2
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64
import sys

print(sys.version)

"""
The mux works by taking in data from various topics at different priority levels. The first priority is the
joystick, then input1, then input2, ... For the joystick you must also hold down a corresponding button 
to be able to control the head since the joystick should be continuously publishing and has 
first priority.
"""

class HeadMux:
    def __init__(self):
        rospy.init_node('head_cmd_mux')

        self.joy_axis = rospy.get_param('~joy_axis', 4) # axes[joy_axis]
        self.joy_button = rospy.get_param('~joy_button', 4) # axes[joy_axis] -> usually map  to same buttons used for control of drive motors
        self.joy_multiplier = rospy.get_param('~joy_multiplier', -0.5) # for adjusting control range

        self.timeout = rospy.get_param('~timeout', 0.5) # for adjusting time in which input control goes to false when no new messages received

        # remap topic names in launch file if necessary
        rospy.Subscriber("joy", Joy, self.joy_cb, queue_size=10)
        self.joy_control = True

        # the following values should be provided in radians by the program generating them
        rospy.Subscriber("input1", Float64, self.input1_cb, queue_size=10)
        self.last_input1 = 0
        rospy.Subscriber("input2", Float64, self.input2_cb, queue_size=10)
        self.last_input2 = 0
        rospy.Subscriber("input3", Float64, self.input3_cb, queue_size=10)
        self.last_input3 = 0

        self.head_cmd_pub = rospy.Publisher("/head_position_controller/command", Float64, queue_size=10)

    def joy_cb(self, data):
        if data.buttons[self.joy_button] == 1:
            self.joy_control = True
            self.head_cmd_pub.publish(data.axes[self.joy_axis]*self.joy_multiplier) # send joy value with multiplier
        else:
            self.joy_control = False

    def input1_cb(self, data):
        if not self.joy_control:
            self.head_cmd_pub.publish(data)
            self.last_input1 = rospy.get_time()

    def input2_cb(self, data):
        if not self.joy_control and (rospy.get_time() - self.last_input1 > self.timeout):
            self.head_cmd_pub.publish(data)
            self.last_input2 = rospy.get_time()

    def input3_cb(self, data):
        if not self.joy_control and (rospy.get_time() - self.last_input1 > self.timeout) and (rospy.get_time() - self.last_input2 > self.timeout):
            self.head_cmd_pub.publish(data)
            self.last_input3 = rospy.get_time()

if __name__=="__main__":
    head_mux = HeadMux()
    rospy.spin()
