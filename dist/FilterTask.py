from Blueprint import *

class STFilter(TaskNode):
    _securityPool = []
    _startDate = ''
    _endDate = ''

    def __init__(self, securityPool, startDate, endDate):
        self._securityPool = securityPool
        self._startDate = startDate
        self._endDate = endDate

    def OnEvolution(self):
        infos = get_extras('is_st', self._securityCode, start_date=self._startDate, end_date=self._endDate)
        for info in infos:
            if info.is_st:
                self._securityPool.remove(info)

        return TaskStatus.Success
