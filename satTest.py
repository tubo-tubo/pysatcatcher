# coding: utf-8
import sat
import unittest

class test_sat(unittest.TestCase):
	def setUp(self):
		orbit = sat.satelite(gslat=43, gslon=141, gselev=50)
		orbit.orbit("METEOSAT-7",
			"1 24932U 97049B   14279.93707767  .00000037  00000-0  00000+0 0  4161",
			"2 24932   9.2709  46.9224 0002598 168.1222 195.3844  1.00275040 62621",
			437.234)

		orbit.data()

if __name__ == '__main__':
    unittest.main()