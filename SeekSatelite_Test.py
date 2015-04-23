import Seeknonn
import SeekSatelite
import unittest
import sys

class teststart(unittest.TestCase):
	
	def testselectfile(self):

		if sys.argv[1]=="debug":
			self.seeksat = Seeknonn.start()

		else:
			self.seeksat = SeekSatelite.start()

		self.seeksat.selectfile("sat")

	def testname(self):

		if sys.argv[1]=="debug":
			self.seeksat = Seeknonn.start()

		else:
			self.seeksat = SeekSatelite.start()

		self.seeksat.satname("METEOSAT-7",
			"1 24932U 97049B   14279.93707767  .00000037  00000-0  00000+0 0  4161",
			"2 24932   9.2709  46.9224 0002598 168.1222 195.3844  1.00275040 62621",
			437.234)


	def testbegin(self):

		if sys.argv[1]=="debug":
			self.seeksat = Seeknonn.start()
		else:
			self.seeksat = SeekSatelite.start()

		self.seeksat.begin()
		self.assertEqual(value,"I'm OK")
		self.assertTrue(value ="Cw")
		self.assertTrue(value ="FM")
		self.assertTrue(value = changeant(a=1,b=2))
		self.assertTrue(value = changefreq(c=4))	
		self.assertTrue(value = "irregular")
		self.assertTrue(value = "cut")

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[1]])