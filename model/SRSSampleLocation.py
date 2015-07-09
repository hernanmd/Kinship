class SRSSampleLocation:

	def __init__(self, freezerType, freezerLocation, samples, location):
    	self.__freezerType = freezerType
		#    assert (type(__freezerType) == object)
    	self.__freezerLocation = freezerLocation
		#    assert (type(__freezerLocation) == object)
    	self.__samples = samples
		#    assert (type(__samples) == object)
    	self.__location = location
		#    assert (type(__location) == SRSRequestSample)
		print "init_:end"

	def freezerType(self):
		self.__freezerType = freezerType

	def freezerLocation(self):
		self.__freezerLocation = freezerLocation

	def samples(self):
		self.__samples = samples

	def location(self):
		self.__location = location