import antenna
import time

class Antenna(object):

	def __init__(self,ant,connect):
		self.ant = antenna.Antenna(ant)
		self.ant.connect(connect)

	#def defmove(self):
		#self.ant.moveazel(0.0,0.0)
		#.time.sleep(1)

	def changeant(self,az,el):
		self.ant.moveazel(az, el)
		self.time.sleep(1)

	def close(self):
		self.ant.moveazel(0.0,0.0)
		self.time.sleep(5)
		self.ant.close()