from abc import ABCMeta
import abc

Bp_debug = True

def enum(**enums):
    return type('Enum',(), enums)

TaskStatus = enum(Unknown = 0, Success = 1, Failed = 2, Running = 3)

class BpUtils:
    @staticmethod
    def GetAllTasksName(tasks):
        if type(tasks) == list:
            names = ""
            for task in tasks:
                names = names + ' ' + task._name
            return names
        else: return ""

    @staticmethod
    def GetTaskStatus(taskStatus):
        if type(taskStatus) == int:
            if taskStatus == 0: return "Unknown"
            elif taskStatus == 1: return "Success"
            elif taskStatus == 2: return "Failed"
            elif taskStatus == 3: return "Running"
        return "Undefined"

class TaskNode:
    __metaclass__ = ABCMeta

    def __init__(self, name = ''):
        self._name = name

    _name = ""
    _status = TaskStatus.Unknown

    def Evolution(self):
        self._status = self.OnEvolution()
        if Bp_debug:
            stat = BpUtils.GetTaskStatus(self._status)
            print "Evolution task node:" + self._name + "[status:"+ stat + "]"
        return self._status

    @abc.abstractmethod
    def OnEvolution(self):
        print "Abstract method NOT implementation,task name: "+self._name
        return TaskStatus.Failed

class Selector(TaskNode):
    _subTasks = []

    def AddTask(self, task, priority = None):
        if not isinstance(task, TaskNode):
            print "Only type of task node is acceptable!"
            return False

        if Bp_debug: print "[Selector]Before add task:" + BpUtils.GetAllTasksName(self._subTasks)

        if priority == None: self._subTasks.append(task)
        else: self._subTasks.insert(priority, task)

        if Bp_debug: print "[Selector]After add task:" + BpUtils.GetAllTasksName(self._subTasks)
        return True

    def RemoveTask(self, index):
        self._subTasks.remove(index)

    def SwitchTask(self, index_from, index_to):
        if Bp_debug: print "Before swap:\n" + BpUtils.GetAllTasksName(self._subTasks)
        self._subTasks[index_from], self._subTasks[index_to] = self._subTasks[index_to], self._subTasks[index_from]
        if Bp_debug: print "After swap:\n" + BpUtils.GetAllTasksName(self._subTasks)

    def OnEvolution(self):
        for task in self._subTasks:
            if task.Evolution() == TaskStatus.Success:
                return TaskStatus.Success
        return TaskStatus.Failed

class Sequence(TaskNode):
    _subTasks = []

    def AddTask(self, task, priority = None):
        if not isinstance(task, TaskNode):
            print "Only type of task node is acceptable!"
            return False

        if Bp_debug: print "[Sequence]Before add task:" + BpUtils.GetAllTasksName(self._subTasks)

        if priority == None: self._subTasks.append(task)
        else: self._subTasks.insert(priority, task)

        if Bp_debug: print "[Sequence]After add task:" + BpUtils.GetAllTasksName(self._subTasks)
        return True

    def RemoveTask(self, index):
        self._subTasks.remove(index)

    def SwapTask(self, index_from, index_to):
        if Bp_debug: print "Before swap:\n" + BpUtils.GetAllTasksName(self._subTasks)
        self._subTasks[index_from], self._subTasks[index_to] = self._subTasks[index_to], self._subTasks[index_from]
        if Bp_debug: print "After swap:\n" + BpUtils.GetAllTasksName(self._subTasks)

    def OnEvolution(self):
        for task in self._subTasks:
            if task.Evolution() != TaskStatus.Success:
                return TaskStatus.Failed
        return TaskStatus.Success