from Blueprint import TaskNode
from Blueprint import TaskStatus
from Blueprint import Selector
from Blueprint import Sequence
import Blueprint

class SetSecurityPoolTask(TaskNode):
    def OnEvolution(self):

        return TaskStatus.Success

class SetOrderTask(TaskNode):
    def OnEvolution(self):
        return TaskStatus.Failed

if __name__ == "__main__":
    Blueprint.Bp_debug = True
    security_filter_task = SetSecuirtyTask("filterSecuiry")
    order_task = SetOrderTask("OrderTask")

    selector = Selector("Selector")
    selector.AddTask(security_filter_task)

    sequencer = Sequence("Sequencer")
    sequencer.AddTask(security_filter_task)
    sequencer.AddTask(order_task)

    sequencer.AddTask(selector,11)
    #sequencer.SwapTask(0,2)
    sequencer.Evolution()
