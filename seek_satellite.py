# coding: utf-8
import sys
import ant
import rad
import sat
import logging

class Start(object):
	def __init__(self):
		self.Radio = rad.radio(typ="IC910",connect="/dev/ttyUSB0")
		self.Antenna = ant.Antenna(ant="RAC805", connect="/dev/ttyUSB1")
		self.Orbit = sat.satelite(gslat=43, gslon=141, gselev=50)

	def select_file(self,filen):
		open("%s.log" % filen)
		logging.basicConfig(filename="%s.log" % filen ,level=logging.INFO , format='%(asctime)s %(message)s')
		logging.info("Making file")
		logging.info("Something error")

	def sat_name(self,satname, tle1, tle2, freq):    #Setting seach sat
		self.Orbit.orbit(satname, tle1, tle2, freq)
		logging.info("Setting complete")
		logging.warning("Something error")

	def begin(self,typ = "IC910",submain = "Sub",modeCWFM = "Cw"):
		self.Radio.seek(typ,modeSubMain,modeCWFM)
		logging.info("All right")
		logging.warning("Something error")

		while True:
			logging.info("Data emission")
			self.Orbit.data()
			value = raw_input("I'm OK")

			if value =="Cw": 
				self.modeCWFM = "CW"
				logging.info("Changed mode CW")
				logging.warning("error")

			elif value =="FM":
				self.modeCWFM = "FM"
				logging.info("Changed mode FM")
				logging.warning("error")

			elif value == changeant(a,b):
				lad = a
				az = b
				self.Antenna.changeant(lad,az)
				logging.info("Changed antenna %s" %(lad,az))
				logging.warning("error") 

			elif value == changefreq(c):
				self.Antenna.changefreq(c)
				logging.info("Changed frequency")
				logging.warning("error")

			elif value == "irregular":
				self.submain = "Main"
				logging.info("Changed mode Main")
				logging.warning("error")

			elif value == "cut":
				Radio.close()
				Antenna.close()
				logging.info("Good night")
				logging.warning("Something bad")
				break


if __name__ == '__main__':
    start().run()
