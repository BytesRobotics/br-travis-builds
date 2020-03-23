#!/usr/bin/env python

# author @Alden Parker
# version 2.1
# This is the emotion engine  node. It is what decides the logic used to simulate emotions in the Garbage Bytes
# for Generative Robotics

from os.path import expanduser
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from std_msgs.msg import Bool
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
import math
import rospy
import time
import random
import argparse
import smach
import smach_ros
import threading


class joy_call:

    # Ros topic /joy/joy callback
    def __init__(self):
        self.old_happy = 0
        self.old_siren = 0
        self.siren = False
        self.old_sound1and2 = 0
        self.old_sound3and4 = 0
        self.old_song = 0

    def joystick_callback(self, data, r):
        # Happy Face on right bumper
        if len(data.buttons) >= 5 and len(data.axes) >= 7:

            if data.buttons[5] == 1 and data.buttons[5] != self.old_happy:
                self.old_happy = 1
                r.userdata.data = 'happy1'
                r.execute()

            elif data.buttons[4] == 1 and data.buttons[4] != self.old_song:
                self.old_song = 1
                r.userdata.data = 'random_song'
                r.execute()

            # Siren on left (or right... I forgot) trigger plus X button
            elif data.buttons[1] == 1 and data.axes[4] == -1 and data.buttons[1] != self.old_siren:
                self.old_siren = 1
                if self.siren:
                    self.siren = False
                    r.userdata.data = 'siren_off'
                    r.execute()

                elif not self.siren:
                    self.siren = True
                    r.userdata.data = 'siren_on'
                    r.execute()

            # Sounds on DPAD
            elif data.axes[7] == 1 and data.axes[7] != self.old_sound1and2:
                self.old_sound1and2 = 1
                r.userdata.data = 'sound1'
                r.execute()

            elif data.axes[7] == -1 and data.axes[7] != self.old_sound1and2:
                self.old_sound1and2 = -1
                r.userdata.data = 'sound2'
                r.execute()

            elif data.axes[6] == 1 and data.axes[6] != self.old_sound3and4:
                self.old_sound3and4 = 1
                r.userdata.data = 'sound3'
                r.execute()

            elif data.axes[6] == -1 and data.axes[6] != self.old_sound3and4:
                self.old_sound3and4 = -1
                r.userdata.data = 'sound4'
                r.execute()

            if data.axes[7] == 0 and data.axes[7] != self.old_sound1and2:
                self.old_sound1and2 = 0

            if data.axes[6] == 0 and data.axes[6] != self.old_sound3and4:
                self.old_sound3and4 = 0

            if data.buttons[1] == 0 and data.buttons[1] != self.old_siren:
                self.old_siren = 0

            if data.buttons[5] == 0 and data.buttons[5] != self.old_happy:
                self.old_happy = 0

            if data.buttons[4] == 0 and data.buttons[4] != self.old_song:
                self.old_song = 0


class imu_call:

    # Ros topic /imu/data callback
    def __init__(self):
        self.time_on = False
        self.start_time = 0

    def imu_callback(self, data, r):
        quaternion = (
            data.orientation.x,
            data.orientation.y,
            data.orientation.z,
            data.orientation.w)

        (roll, pitch, yaw) = euler_from_quaternion(quaternion)

        roll = math.degrees(roll)
        pitch = math.degrees(pitch)
        yaw = math.degrees(yaw)

        if ((roll > 60 or pitch > 60) or (roll < -60 or pitch < -60)) and self.time_on is False:
            self.time_on = True
            self.start_time = time.time()
        elif ((roll < 60 or pitch < 60) or (roll > -60 or pitch > -60)) and self.time_on is True:
            if -60 < roll < 60 and -60 < pitch < 60 and r.userdata.siren_state == 'warble':
                self.time_on = False
                r.userdata.data = 'warble_finish'
                r.execute()

            elif (time.time() - self.start_time) >= 1 and r.userdata.siren_state != 'warble':
                r.userdata.data = 'warble'
                r.execute()


# Make router machine
def router():
    r = smach.StateMachine(outcomes=['succeeded'])  # Joy smach machine for Joystick action
    r.userdata.data = None
    r.userdata.siren_state = False

    # Open the joy container
    with r:
        # Add states to joy
        smach.StateMachine.add('handler',
                               handler(),
                               transitions={'happy_face': 'happy',
                                            'siren': 'siren',
                                            'sound': 'sound',
                                            'done': 'succeeded',
                                            'err': 'error'})

        smach.StateMachine.add('siren',
                               siren(),
                               transitions={'done': 'succeeded',
                                            'err': 'error'})

        smach.StateMachine.add('happy',
                               happy(),
                               transitions={'done': 'succeeded',
                                            'err': 'error'})

        smach.StateMachine.add('sound',
                               sound(),
                               transitions={'done': 'succeeded',
                                            'err': 'error'})

        smach.StateMachine.add('error',
                               error(),
                               transitions={'done': 'succeeded'})

    return r


# Data Handler
class handler(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['happy_face', 'siren', 'sound', 'done', 'err'],
                             input_keys=['data'],
                             output_keys=['siren_state', 'sound_name', 'happy_animation', 'err'])

    def execute(self, userdata):
        try:
            # Happy Face on right bumper
            if userdata.data == "happy1":
                userdata.happy_animation = 'happy1'
                return 'happy_face'

            # Siren on left (or right... I forgot) trigger plus X button
            elif userdata.data == "siren_off":
                userdata.siren_state = False
                return 'siren'

            elif userdata.data == "siren_on":
                userdata.siren_state = True
                return 'siren'

            # Sounds on DPAD
            elif userdata.data == "sound1":
                userdata.sound_name = 'sound1'
                return 'sound'

            elif userdata.data == "sound2":
                userdata.sound_name = 'sound2'
                return 'sound'

            elif userdata.data == "sound3":
                userdata.sound_name = 'sound3'
                return 'sound'

            elif userdata.data == "sound4":
                userdata.sound_name = 'sound4'
                return 'sound'

            elif userdata.data == "random_song":
                userdata.sound_name = 'rand_song'
                return 'sound'

            elif userdata.data == 'warble':
                userdata.siren_state = 'warble'
                return 'siren'

            elif userdata.data == 'warble_finish':
                userdata.siren_state = 'warble_finish'
                return 'siren'

            return 'done'

        except Exception as e:
            userdata.err = e
            return 'err'


# Siren Handler
class siren(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['done', 'err'],
                             input_keys=['siren_state'],
                             output_keys=['err'])

        self.finish = False
        self.warble_proc = None
        self.warble_on = 5
        self.warble_off = 2

    def execute(self, userdata):
        try:
            if userdata.siren_state is False:
                siren_pub.publish(Bool(False))
                return 'done'

            elif userdata.siren_state is True:
                siren_pub.publish(Bool(True))
                return 'done'

            elif userdata.siren_state == 'warble':
                # Start Warble Thread
                if self.warble_proc is None:
                    self.warble_proc = threading.Thread(target=self.warble, args=(siren_pub,))
                    self.warble_proc.start()

                return 'done'

            elif userdata.siren_state == 'warble_finish':
                # Stop Warble Thread
                self.finish = True
                self.warble_proc.join()
                time.sleep(0.1)
                self.warble_proc = None
                self.finish = False

                return 'done'

        except Exception as e:
            userdata.err = e
            return 'err'

    def warble(self, s):
        while True:
            if self.finish:
                break

            s.publish(Bool(True))

            for x in range(0, self.warble_on):
                time.sleep(1)

                if self.finish:
                    break

            s.publish(Bool(False))

            for x in range(0, self.warble_off):
                time.sleep(1)

                if self.finish:
                    break


# Happy Animation Handler
class happy(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['done', 'err'],
                             input_keys=['happy_animation'],
                             output_keys=['err'])

    def execute(self, userdata):
        try:
            if userdata.happy_animation == 'happy1':
                face_pub.publish(String("happy1"))
                return 'done'

        except Exception as e:
            userdata.err = e
            return 'err'


# Sound Handler
class sound(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['done', 'err'],
                             input_keys=['sound_name'],
                             output_keys=['err'])

    def execute(self, userdata):
        try:
            if userdata.sound_name == 'sound1':
                sound_pub.publish(String("r2d2-twiddle-short"))
                return 'done'

            elif userdata.sound_name == 'sound2':
                sound_pub.publish(String("r2d2-twiddle-shorter"))
                return 'done'

            elif userdata.sound_name == 'sound3':
                sound_pub.publish(String("carlos_ad_sucks_dick"))
                return 'done'

            elif userdata.sound_name == 'sound4':
                sound_pub.publish(String("wa-wallie"))
                return 'done'

            elif userdata.sound_name == 'rand_song':
                music_pub.publish(String("random"))
                return 'done'

        except Exception as e:
            userdata.err = e
            return 'err'


# Error Handler
class error(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['done'],
                             input_keys=['err'])

    def execute(self, userdata):
        rospy.logerr('finite_emotion_engine Error:')
        for x in userdata.err:
            rospy.logerr(x)

        return 'done'


if __name__ == '__main__':
    # Get Args
    # parser = argparse.ArgumentParser(description='Identify testing of node.')
    # parser.add_argument('--test',
    #                     help='Test Mode',
    #                     action='store_true')
    #
    # args = parser.parse_args()

    # Init Ros Node
    rospy.init_node('finite_emotion_engine',
                    anonymous=True)

    router = router()  # Get Router Machine

    imu_call = imu_call()  # Get Callback and Logic
    joy_call = joy_call()  # Get Callback and Logic

    # server_router = smach_ros.IntrospectionServer('debug_finite_server', router, '/finite_behavior_engine')

    # server_router.start()

    face_pub = rospy.Publisher('/behavior_engine/face',
                               String,
                               queue_size=3)

    sound_pub = rospy.Publisher('/behavior_engine/sounds',
                                String,
                                queue_size=3)

    music_pub = rospy.Publisher('/behavior_engine/music',
                                String,
                                queue_size=3)

    siren_pub = rospy.Publisher('/siren',
                                Bool,
                                queue_size=3)

    fan = rospy.Publisher('/fan',
                          Bool,
                          queue_size=3,
                          latch=True)

    fan.publish(Bool(True))

    rospy.Subscriber("/joy/joy", Joy, joy_call.joystick_callback, router)  # Subscribe to topic
    rospy.Subscriber("/imu/data", Imu, imu_call.imu_callback, router)  # Subscribe to topic

    rospy.spin()
    # server_router.stop()
