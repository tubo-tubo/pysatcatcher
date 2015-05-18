#import antenna
import time

class Antenna(object):

	def __init__(self,ant,connect):
		print("ant"+str(ant))
		print("connect:"+str(connect))
		#self.ant = antenna.Antenna(ant)
		#self.ant.connect(connect)

	#def defmove(self):
		#print("defmode")
		#self.ant.moveazel(0.0,0.0)
		#time.sleep(1)
		#return True

	def changeant(self,az,el):
		print("changeant"+str(az)+" "+str(el))
		#self.ant.moveazel(az, el)
		time.sleep(1)
		return True

	def close(self):
		print("close")
		#self.ant.moveazel(0.0,0.0)
		time.sleep(5)
		#self.ant.close()
		return True