import unittest
from SRSData import *
from model.SRSMarker import SRSMarker


class TestSRSMarker(unittest.TestCase):
    def setUp(self):
        print "setUp_:begin"
        self.srsMarkerList = SRSData().readmarkercsv('data\SRS_Markers.csv')
        print "setUp_:end"

    def test_create(self):
        for srsmarker in self.srsMarkerList:
            self.assertIsInstance(srsmarker, SRSMarker)

    def test_sourcePlatform(self):
        self.assertTrue(self.srsMarkerList[0].sourcePlatform(), "M")
        self.assertTrue(self.srsMarkerList[1].sourcePlatform(), "F")

    def test_markerName(self):
        self.assertTrue(self.srsMarkerList[0].markerName(), "M")
		self.assertTrue(self.srsMarkerList[1].markerName(), "M")

	def test_markerValue(self):
		self.assertTrue(self.srsMarkerList[0].markerValue(), "canis lupus")
		self.assertTrue(self.srsMarkerList[1].markerValue(), "bos taurus")
	
	def test_requestSample(self):
		self.assertTrue(self.srsMarkerList[0].requestSample(), "canis lupus")
		self.assertTrue(self.srsMarkerList[1].requestSample(), "bos taurus")

	def test_chromosomeName(self):
		self.assertTrue(self.srsMarkerList[0].chromosomeName(), "canis lupus")
		self.assertTrue(self.srsMarkerList[1].chromosomeName(), "bos taurus")

	if __name__ == '__main__':
		unittest.main()