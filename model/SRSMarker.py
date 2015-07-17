class SRSMarker:

	def __init__(self, sourcePlatform, markerName, markerValue, requestSample, chromosomeName):
		self.__sourcePlatform = sourcePlatform
		self.__markerName = markerName
		self.__markerValue = markerValue
		self.__requestSample = requestSample
		self.__chromosomeName = chromosomeName

	def sourcePlatform(self, sourcePlatform):
		self.__sourcePlatform = sourcePlatform

	def markerName(self):
		return self.__markerName

	def markerValue(self):
		return self.__markerValue

	def requestSample(self):
		return self.__requestSample
		
	def chromosomeName(self):
		return self.__chromosomeName


