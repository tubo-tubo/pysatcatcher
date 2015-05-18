import seek_none
import seek_satellite
import unittest
import sys

class TestStart(unittest.TestCase):
	
	def test_select_file(self):
		if sys.argv[1]=="debug":
			self.seeksat = seek_none.Start()

		else:
			self.seeksat = seek_satellite.Start()

		self.seeksat.select_file("sat")

	def test_name(self):

		if sys.argv[1]=="debug":
			self.seeksat = seek_none.Start()

		else:
			self.seeksat = seek_satellite.Start()

		self.seeksat.sat_name("METEOSAT-7",
			"1 24932U 97049B   14279.93707767  .00000037  00000-0  00000+0 0  4161",
			"2 24932   9.2709  46.9224 0002598 168.1222 195.3844  1.00275040 62621",
			437.234)


	def test_begin(self):

		if sys.argv[1]=="debug":
			self.seeksat = seek_none.Start()
		else:
			self.seeksat = seek_satellite.Start()

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