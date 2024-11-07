from yasmin import Blackboard

from yasmin_ros import ActionState
from yasmin_ros.ros_logs import set_ros_loggers
from yasmin_ros.basic_outcomes import SUCCEED, ABORT, CANCEL
from astro_actions import ACTION_NAMES

from astro_action_interfaces.action import ManualControl
class ManualControlState(ActionState):
    """
    Class representing the state of the Fibonacci action.

    Inherits from ActionState and implements methods to handle the
    Fibonacci action in a finite state machine.

    Attributes:
        None
    """

    def __init__(self) -> None:
        """
        Initializes the Connect State.


        Parameters:
            None

        Returns:
            None
        """
        super().__init__(
            ManualControl,  # action type
            ACTION_NAMES.MANUAL_CONTROL,  # action name
            self.create_goal_handler,  # callback to create the goal
            None,  # outcomes. Includes (SUCCEED, ABORT, CANCEL)
            self.response_handler,  # callback to process the response
            self.print_feedback,  # callback to process the feedback
        )

    def create_goal_handler(self, blackboard: Blackboard) -> ManualControl.Goal:
        
        goal = ManualControl.Goal()
        return goal

    def response_handler(
        self, blackboard: Blackboard, response: ManualControl.Result
    ) -> str:

        return SUCCEED

    def print_feedback(
        self, blackboard: Blackboard, feedback: ManualControl.Feedback
    ) -> None:
        ...