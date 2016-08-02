from Blueprint import *

class IsSTSecurity(TaskNode):
    _securityCode = ''
    _startDate = ''
    _endDate = ''

    def __init__(self, securityCode, startDate, endDate):
        self._securityCode = securityCode
        self._startDate = startDate
        self._endDate = endDate

    def OnEvolution(self):
        info = get_extras('is_st', self._securityCode, start_date=self._startDate, end_date=self._endDate)
