import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property

class Holonomicrobotactuator(morse.core.actuator.Actuator):
    """Write here the general documentation of your actuator.
    It will appear in the generated online documentation.
    """
    _name = "Holonomicrobotactuator"
    _short_desc = "Actuator based on a kinematic description of the motion equations for an omnidirectional robot with omniwheels"

    # define here the data fields required by your actuator
    # format is: field name, initial value, type, description
    add_data('w1', 0, 'float', 'The rotational speed of the first wheel')
    add_data('w2', 0, 'float', 'The rotational speed of the second wheel')
    add_data('w3', 0, 'float', 'The rotational speed of the third wheel')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        morse.core.actuator.Actuator.__init__(self, obj, parent)

        # Do here actuator specific initializations

        self._target_count = 0 # dummy internal variable, for testing purposes

        logger.info('Component initialized')

    def default_action(self):
        """ Main loop of the actuator.

        Implements the component behaviour
        """

        # check if we have an on-going asynchronous tasks...
        if self._target_count and self.local_data['counter'] > self._target_count:
            self.completed(status.SUCCESS, self.local_data['counter'])

        # implement here the behaviour of your actuator
        self.local_data['counter'] += 1
