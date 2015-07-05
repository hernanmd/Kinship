import csv
import sys
import os
from pprint import pprint

pprint(os.getcwd())
pprint(sys.path)

from datetime import datetime
from model.SRSUser import (SRSUser)
from model.SRSAnimal import SRSAnimal
from model.SRSSampleLocation import SRSSampleLocation

srsUserList = []
srsAnimalsList = []
srsSampleLocations = []


class SRSData(object):
    @staticmethod
    def readuserscsv(filename):
        with open(filename, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ';')
            # Skip header line
            csvreader.next()
            print "Reading CSV file..."
            for row in csvreader:
                srsUserList.append(SRSUser(row[0], row[1], row[2]))
            print "Done"
        return srsUserList

    @staticmethod
    def readanimalscsv(filename):
        with open(filename, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ";")
            csvreader.next()
            print "Reading Animals..."
            for row in csvreader:
                date_object = datetime.strptime(row[2], "%d/%m/%Y")
                srsAnimalsList.append(SRSAnimal(row[0], row[1], date_object, row[3], row[4], row[5]))
            print "Done"
        return srsAnimalsList

    @staticmethod
    def readSampleLocationsCSV(filename):
        with open(filename, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ';')
            csvreader.next()
            print "Reading Sample Locations..."
            for row in csvreader:
                srsSampleLocations.append(SRSSampleLocation(row[0], row[1], row[2]))
            print "Done"
        return srsSampleLocations
