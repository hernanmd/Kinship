import unittest
from SRSData import *
from model.SRSUser import SRSUser

class TestSRSUser(unittest.TestCase):

	def setUp(self):
		print "setUp_:begin"
		self.srsUserList = SRSData().readCSV('data\SRS_Users.csv')
		print "setUp_:end"
		
	def test_equal(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_create(self):
		for srsUser in self.srsUserList:
			self.assertIsInstance(srsUser, SRSUser)

if __name__ == '__main__':
	unittest.main()
