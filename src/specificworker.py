#
# Copyright (C) 2018 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os, Ice, traceback, time

#sys.path.append('/usr/local/lib/python3.6/site-packages')

from morse.builder import *

from PySide import QtCore, QtGui
from genericworker import *

ROBOCOMP = ''
try:
	ROBOCOMP = os.environ['ROBOCOMP']
except:
	print ('$ROBOCOMP environment variable not set, using the default value /opt/robocomp')
	ROBOCOMP = '/opt/robocomp'
if len(ROBOCOMP)<1:
	print ('genericworker.py: ROBOCOMP environment variable not set! Exiting.')
	sys.exit()


preStr = "-I"+ROBOCOMP+"/interfaces/ --all "+ROBOCOMP+"/interfaces/"
Ice.loadSlice(preStr+"DifferentialRobot.ice")
from RoboCompDifferentialRobot import *
Ice.loadSlice(preStr+"Laser.ice")
from RoboCompLaser import *
Ice.loadSlice(preStr+"JointMotor.ice")
from RoboCompJointMotor import *


from differentialrobotI import *
from laserI import *
from jointmotorI import *

class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)
		self.timer.timeout.connect(self.compute)
		self.Period = 2000
		self.timer.start(self.Period)

	def setParams(self, params):
		env = Environment('indoors-1/indoor-1')
		env.set_camera_location([5, -5, 6])
		env.set_camera_rotation([1.0470, 0, 0.7854])
		#try:
		#	par = params["InnerModelPath"]
		#	innermodel_path=par.value
		#	innermodel = InnerModel(innermodel_path)
		#except:
		#	traceback.print_exc()
		#	print "Error reading config params"
		return True

	@QtCore.Slot()
	def compute(self):
		print ('SpecificWorker.compute...')
		#try:
		#	self.differentialrobot_proxy.setSpeedBase(100, 0)
		#except Ice.Exception, e:
		#	traceback.print_exc()
		#	print e
		return True


	#
	# correctOdometer
	#
	def correctOdometer(self, x, z, alpha):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# getBasePose
	#
	def getBasePose(self):
		#
		# YOUR CODE HERE
		#
		x = int()
		z = int()
		alpha = float()
		return [x, z, alpha]

	#
	# resetOdometer
	#
	def resetOdometer(self):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# setOdometer
	#
	def setOdometer(self, state):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# getBaseState
	#
	def getBaseState(self):
		#
		# YOUR CODE HERE
		#
		state = TBaseState()
		return state


	#
	# setOdometerPose
	#
	def setOdometerPose(self, x, z, alpha):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# stopBase
	#
	def stopBase(self):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# setSpeedBase
	#
	def setSpeedBase(self, adv, rot):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# getLaserData
	#
	def getLaserData(self):
		ret = TLaserData()
		#
		# YOUR CODE HERE
		#
		return ret


	#
	# getLaserConfData
	#
	def getLaserConfData(self):
		ret = LaserConfData()
		#
		# YOUR CODE HERE
		#
		return ret


	#
	# getLaserAndBStateData
	#
	def getLaserAndBStateData(self):
		ret = TLaserData()
		#
		# YOUR CODE HERE
		#
		bState = RoboCompDifferentialRobot.TBaseState()
		return [ret, bState]

	#
	# getAllMotorParams
	#
	def getAllMotorParams(self):
		ret = MotorParamsList()
		#
		# YOUR CODE HERE
		#
		return ret


	#
	# getAllMotorState
	#
	def getAllMotorState(self):
		#
		# YOUR CODE HERE
		#
		mstateMap = MotorStateMap()
		return mstateMap


	#
	# getMotorParams
	#
	def getMotorParams(self, motor):
		ret = MotorParams()
		#
		# YOUR CODE HERE
		#
		return ret


	#
	# getMotorState
	#
	def getMotorState(self, motor):
		ret = MotorState()
		#
		# YOUR CODE HERE
		#
		return ret


	#
	# setSyncVelocity
	#
	def setSyncVelocity(self, listGoals):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# setZeroPos
	#
	def setZeroPos(self, name):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# getBusParams
	#
	def getBusParams(self):
		ret = BusParams()
		#
		# YOUR CODE HERE
		#
		return ret


	#
	# setSyncZeroPos
	#
	def setSyncZeroPos(self):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# setSyncPosition
	#
	def setSyncPosition(self, listGoals):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# getMotorStateMap
	#
	def getMotorStateMap(self, mList):
		ret = MotorStateMap()
		#
		# YOUR CODE HERE
		#
		return ret


	#
	# setPosition
	#
	def setPosition(self, goal):
		#
		# YOUR CODE HERE
		#
		pass


	#
	# setVelocity
	#
	def setVelocity(self, goal):
		#
		# YOUR CODE HERE
		#
		pass





