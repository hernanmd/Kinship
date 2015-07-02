import unittest
from SRSData import *
from model.SRSAnimal import SRSAnimal

class TestSRSAnimals(unittest.TestCase):
    def setUp(self):
        print "setUp_:begin"
        self.srsAnimalsList = SRSData().readanimalscsv('data\SRS_Animals.csv')
        print "setUp_:end"

    def test_create(self):
        for srsanimal in self.srsAnimalsList:
            self.assertIsInstance(srsanimal, SRSAnimal)

if __name__ == '__main__':
    unittest.main()
