import unittest
from SRSData import *
from model.SRSSampleLocation import SRSSampleLocation


class TestSRSSampleLocation(unittest.TestCase):
    def setUp(self):
        print ("setUp_:begin")
        self.srsSampleLocationList = SRSData().readSampleLocationsCSV('data\SRS_Sample_Locations.csv')
        print ("setUp_:end")

    def test_equal(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_create(self):
        for srsSampleLocations in self.srsSampleLocationList:
            self.assertIsInstance(srsSampleLocations, SRSSampleLocation)


if __name__ == '__main__':
    unittest.main()
