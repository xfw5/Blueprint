from Blueprint import *

class FilterSTSecurity(TaskNode):
    _securityCodeList = ''
    _startDate = ''
    _endDate = ''

    def __init__(self, securityCodeList, startDate, endDate):
        self._securityCodeList = securityCodeList
        self._startDate = startDate
        self._endDate = endDate

    def OnEvolution(self):
        infos = get_extras('is_st', self._securityCodeList, start_date=self._startDate, end_date=self._endDate)
        infos[infos == False] = None
        infos.dropna(axis=1)

        return TaskStatus.Success