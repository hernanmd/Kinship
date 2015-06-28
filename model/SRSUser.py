class SRSUser:
	__userRole = 0
	#assert(type(__userRole)==object)
	
	def __init__(self,name,password,dni):
		self.__name = name
		self.__password = password
		self.__dni = dni
		print "init_:end"
