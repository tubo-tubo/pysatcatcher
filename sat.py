# coding: utf-8
import Orbitcalc

class Satellite(object):
	def __init__(self, gslat,gslon,gselev):
		self.orbit = Orbitcalc.Orbitcalc(gslat, gslon, gselev)
		
	def orbit(self,satname,tle1,tle2,freq):
		self.orbit.SatInfo(satname, tle1, tle2, freq)

	def data(self):
		satlat, satlon, satfreq,aos,los,elmax = self.orbit.CalcObserve()
		print("satlat ="+satlat)
		print("satlon ="+satlon)
		print("satfreq ="+satfreq)
		print("aos ="+str(aos.strftime("%H:%M:%S")))
		print("los ="+str(los.strftime("%H:%M:%S")))
		print("elmax ="+elmax)

#orbit = Orbitcalc.Orbitcalc(gslat='43', gslon='141', gselev='50')
#orbit.SatInfo("METEOSAT-7","1 24932U 97049B   14279.93707767  .00000037  00000-0  00000+0 0  4161","2 24932   9.2709  46.9224 0002598 168.1222 195.3844  1.00275040 62621",'437.234')
#satlat, satlon, satfreq,aos,los,elmax = orbit.CalcObserve()