# coding: utf-8
import rad_none
import rad
import unittest
import sys

class  test_rad(unittest.TestCase):

	def test_seek1(self):
		if sys.argv[1] == "debug":
			Radio = rad_none.Radio(connect="/dev/ttyUSB1")

		else :
			Radio = rad.Radio(connect="/dev/ttyUSB1")

		Radio.seek(typ="IC910", modeSubMain="Sub", modeCWFM="Cw")
		#self.assertTrue(self.Radio.currentMode())
		#self.assertTrue(self.Radio.currentMode())
		self.assertEqual(Radio.change_freq(437.485), 437.485)
		self.assertTrue(Radio.seek)
		self.assertTrue(Radio.close())
		

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[1]])