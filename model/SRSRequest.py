
class SRSRequest:    

    def __init__(self, requestState, requestName, requestOwner, requestReport):
        self.__requestState = requestState
        self.__requestName = requestName
        self.__requestOwner = requestOwner
        self.__requestReport = requestReport

    def requestState(self):
       return self.__requestState

    def requestName(self, requestName):
        self.__requestName = requestName

    def requestName(self):
        return self.__requestName

    def requestOwner(self, requestOwner):
        self.__requestOwner = requestOwner

    def requestOwner(self):
        return self.__requestOwner

    def requestReport(self, requestReport):
        self.__requestReport = requestReport

    def requestReport(self):
        return self.__requestReport