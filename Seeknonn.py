# coding: utf-8
import sys
import antnone
import radnonn
import sat
import logging

class start(object):
	def __init__(self):
		self.Radio = radnonn.Radio(connect="/dev/ttyUSB1")
		self.Antenna = antnone.Antenna(ant="RAC805", connect="/dev/ttyUSB1")
		self.orbit = sat.satelite(gslat=43, gslon=141, gselev=50)

	def selectfile(self,filen):
		open("%s.log" % filen)
		logging.basicConfig(filename="%s.log" % filen ,level=logging.INFO , format='%(asctime)s %(message)s')
		logging.info("Making file")
		logging.info("Something error")

	def satname(self,satname, tle1, tle2, freq):    #Setting seach sat
		self.orbit.orbit(satname, tle1, tle2, freq)
		logging.info("Setting complete")
		logging.warning("Something error")

	def begin(self,typ = "IC910",submain = "Sub",modeCWFM = "CW"):
		self.Radio.seek(typ,submain,modeCWFM)
		logging.info("All right")
		logging.warning("Something error")

		while True:
			logging.info("Data emission")
			self.orbit.data()
			#value = raw_input("I'm OK")
			value = print("I'm OK")

			if value =="Cw": 
				self.modeCWFM = "CW"
				return(True)
				logging.info("Changed mode CW")
				logging.warning("error")

			elif value =="FM":
				self.modeCWFM = "FM"
				return(True)
				logging.info("Changed mode FM")
				logging.warning("error")

			elif value == changeant(a,b):
				lad = a
				az = b
				self.Antenna.changeant(lad,az)
				return(True)
				logging.info("Changed antenna %s" %(lad,az))
				logging.warning("error") 

			elif value == changefreq(c):
				self.Antenna.changefreq(c)
				return(True)
				logging.info("Changed frequency")
				logging.warning("error")

			elif value == "irregular":
				self.submain = "Main"
				return(True)
				logging.info("Changed mode Main")
				logging.warning("error")

			elif value == "cut":
				self.Radio.close()
				self.Antenna.close()
				return(True)
				logging.info("Good night")
				logging.warning("Something bad")
				break


if __name__ == '__main__':
    start().run()