# coding: utf-8
import unittest
import sys
#if sys.argv[1] == 'debug':
#    print("debu")
import ant_none
#else:
import ant

class TestAntenna(unittest.TestCase):

    def test_move(self):
        if sys.argv[1] == "debug":
            self.antenna = ant_none.Antenna(ant="RAC805", connect="/dev/ttyUSB1")
        else:
            self.antenna = ant.Antenna(ant="RAC805", connect="/dev/ttyUSB1")
            
        self.assertTrue(self.antenna.changeant(10.0,0.0))
        self.assertTrue(self.antenna.changeant(-10.0,-20.0))

    def test_close(self):
        if sys.argv[1] == "debug":
            self.antenna = ant_none.Antenna(ant="RAC805", connect="/dev/ttyUSB1")
        else:
            self.antenna = ant.Antenna(ant="RAC805", connect="/dev/ttyUSB1")

        self.assertTrue(self.antenna.close())

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[1]])