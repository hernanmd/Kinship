import unittest
from SRSData import *
from model.SRSAnimal import SRSAnimal
from datetime import datetime


class TestSRSAnimals(unittest.TestCase):
    def setUp(self):
        print "setUp_:begin"
        self.srsAnimalsList = SRSData().readanimalscsv('data\SRS_Animals.csv')
        print "setUp_:end"

    def test_create(self):
        for srsanimal in self.srsAnimalsList:
            self.assertIsInstance(srsanimal, SRSAnimal)

    def test_sex(self):
        self.assertTrue(self.srsAnimalsList[0].sex(), "M")
        self.assertTrue(self.srsAnimalsList[1].sex(), "F")

    def test_borndate(self):
        for srsanimal in self.srsAnimalsList:
            self.assertIsInstance(srsanimal.borndate(), datetime)

if __name__ == '__main__':
    unittest.main()

