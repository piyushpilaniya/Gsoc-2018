#! /usr/bin/env morseexec


from morse.builder import *
from omni.builder.robots import Holonomicrobot, Target
from omni.builder.actuators import Holonomicrobotactuator

robot = Holonomicrobot()
robot.add_default_interface('socket')

pose = Pose()
robot.append(pose)

robot.add_default_interface('socket')

target = Target()
target.translate(x=-2)

env = Environment('sandbox', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
