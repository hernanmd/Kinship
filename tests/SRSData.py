import csv
from model.SRSUser import (SRSUser)

srsUserList = []

class SRSData(object):

	def readCSV(self,fileName):
		with open(fileName, 'rb') as csvfile:
			csvReader = csv.reader(csvfile, delimiter=';')
			#Skip header line
			csvReader.next()
			for row in csvReader:
				print "Reading CSV file..."
				srsUserList.append(SRSUser(row[0],row[1],row[2]))
				print "Done"
		return srsUserList
