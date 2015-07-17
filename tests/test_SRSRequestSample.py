import unittest
from SRSData import *
from model.SRSRequestSample import SRSRequestSample
from datetime import datetime


class TestSRSRequestSample(unittest.TestCase):
    def setUp(self):
        print "setUp_:begin"
        self.srsRequestSampleList = SRSData().readrequestsamplecsv('data\SRS_RequestSample.csv')
        print "setUp_:end"

    def test_create(self):
        for srsrequestsample in self.srsRequestSampleList:
            self.assertIsInstance(srsrequestsample, SRSRequestSample)

    def test_sampleRuns(self):
        self.assertTrue(self.srsRequestSampleList[0].sampleRuns(), "M")
        self.assertTrue(self.srsRequestSampleList[1].sampleRuns(), "F")

    def test_sampleMarkers(self):
        self.assertTrue(self.srsRequestSampleList[0].sampleMarkers(), "M")
		self.assertTrue(self.srsRequestSampleList[1].sampleMarkers(), "M")

	def test_sampleIndividual(self):
		self.assertTrue(self.srsRequestSampleList[0].sampleIndividual(), "canis lupus")
		self.assertTrue(self.srsRequestSampleList[1].sampleIndividual(), "bos taurus")
	
	def test_sampleCode(self):
		self.assertTrue(self.srsRequestSampleList[0].sampleCode(), "canis lupus")
		self.assertTrue(self.srsRequestSampleList[1].sampleCode(), "bos taurus")
	
	def test_sampleCreationDate(self):
		for srsrequestsample in self.srsRequestSampleList:
            self.assertIsInstance(srsrequestsample.sampleCreationDate(), datetime)
	
	def test_sampleBarCode(self):
		self.assertTrue(self.srsRequestSampleList[0].sampleBarCode(), "canis lupus")
		self.assertTrue(self.srsRequestSampleList[1].sampleBarCode(), "bos taurus")
		
	def test_dateEntered(self):
		for srsrequestsample in self.srsRequestSampleList:
            self.assertIsInstance(srsrequestsample.dateEntered(), datetime)
			
	def test_receiveBy(self):
		self.assertTrue(self.srsRequestSampleList[0].receiveBy(), "canis lupus")
		self.assertTrue(self.srsRequestSampleList[1].receiveBy(), "bos taurus")
	
	def test_location(self):
		self.assertTrue(self.srsRequestSampleList[0].location(), "canis lupus")
		self.assertTrue(self.srsRequestSampleList[1].location(), "bos taurus")

	if __name__ == '__main__':
		unittest.main()