from morse.builder.creator import ActuatorCreator

class Holonomicrobotactuator(ActuatorCreator):
    _classpath = "omni.actuators.HolonomicRobotActuator.Holonomicrobotactuator"
    _blendname = "HolonomicRobotActuator"

    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name)

