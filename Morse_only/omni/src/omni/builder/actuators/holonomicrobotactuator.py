from morse.builder.creator import ActuatorCreator

class Holonomicrobotactuator(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "omni.actuators.holonomicrobotactuator.Holonomicrobotactuator",\
                                 "holonomicrobotactuator")
