#! /usr/bin/env morseexec


from morse.builder import *
from omni.builder.robots import Holonomicrobot, Target
from omni.builder.actuators import Holonomicrobotactuator
from morse.helpers import *

robot = Holonomicrobot()
robot.add_default_interface('socket')

pose = Pose()
robot.append(pose)

robot.add_default_interface('socket')

camera=VideoCamera()
camera.translate(z=0.5)
robot.append(camera)

camera2= DepthCamera()
camera2.translate(z = 1)
camera2.properties(cam_width = 640, cam_height = 480)
camera2.frequency(15)
robot.append(camera2)
camera.add_stream('socket')


sick = Sick()
sick.translate(z=2)
robot.append(sick)
sick.add_interface('socket')

#target = Target()
#target.translate(x=-2)

env = Environment('sandbox', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
