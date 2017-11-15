#!/usr/bin/env python

# Copyright 2017 Open Source Robotics Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# This is a rewrite of the script 'joystick_translator'


import rospy
from prius_msgs.msg import Control


STEERING_AXIS = 0
THROTTLE_AXIS = 4


class Translator:
    def __init__(self, operations):
        self.pub = rospy.Publisher('prius', Control, queue_size=1)
        self.last_published_time = rospy.get_rostime()
        self.operations = operations
        self.timer = rospy.Timer(rospy.Duration(1./20.), self.timer_callback)
        
    def timer_callback(self, event):
        if self.last_published_time < rospy.get_rostime() + rospy.Duration(1.0/20.):
            self.move()

    def move(self):
        command = Control()

        command.throttle = self.operations[0]
        command.brake = self.operations[1]
        command.shift_gears = self.operations[2]
        command.steer = self.operations[3]

        self.pub.publish(command)


if __name__ == '__main__':
    rospy.init_node('rcv', anonymous=True)

    print("Let's move your RCV")
    throttle = input("Input your throttle: ")
    brake = input("Input your brake: ")
    shift_gears = input("Input your shift_gears: ")
    steer = input("Input your steer: ")
    operations = [throttle, brake, shift_gears, steer]

    t = Translator(operations)
    rospy.spin()
