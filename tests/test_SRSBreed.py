import unittest
from SRSData import *
from model.SRSBreed import SRSBreed


class TestSRSBreed(unittest.TestCase):
    def setUp(self):
        print ("setUp_:begin")
        self.srsBreedList = SRSData().readbreedscsv('data\SRS_Breeds.csv')
        print ("setUp_:end")

    def test_create(self):
        for srsBreed in self.srsBreedList:
            self.assertIsInstance(srsBreed, SRSBreed)

    def test_species(self):
        self.assertTrue(self.srsBreedList[0].species(), "Bos Taurus")
        self.assertTrue(self.srsBreedList[1].species(), "Bos Taurus")
        self.assertTrue(self.srsBreedList[2].species(), "Bos Taurus")

    def test_synonyms(self):
        self.assertTrue(self.srsBreedList[0].synonyms(), "")
        self.assertTrue(self.srsBreedList[1].synonyms(), "")
        self.assertTrue(self.srsBreedList[-1].synonyms(), "")

    def test_name(self):
        self.assertTrue(self.srsBreedList[0].name(), "Holstein")
        self.assertTrue(self.srsBreedList[1].name(), "Hungarian Grey")
        self.assertTrue(self.srsBreedList[2].name(), "Criollo Ecuatoriano")

if __name__ == '__main__':
    unittest.main()


