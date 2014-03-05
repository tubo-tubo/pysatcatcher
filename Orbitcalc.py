# -*- coding: utf-8 -*-

import ephem
import math
import datetime

ENCODING = 'utf-8'

degreeconv = 180/math.pi
#
home = ephem.Observer()
home.lat = '43.134694'
home.lon = '141.248194'
home.elev = 50
calctime_utc = datetime.datetime.now()
satresult = []


class Orbitcalc(object):
    _gslat = ''
    _gslon = ''
    _gselev = ''
    _satname = ''
    _tle1 = ''
    _tle2 = ''
    _frequency = ''

    def __init__(self, gslat, gslon, gselev):
        self._gslat = str(gslat)
        self._gslon = str(gslon)
        self._gselev = str(gselev)

    def SatInfo(self, satname, tle1, tle2, frequency):
        self._satname = str(satname)
        self._tle1 = str(tle1)
        self._tle2 = str(tle2)
        self._frequency = str(frequency)

    def dopplershift(self, c, rangerate):
        return (c/(c + rangerate))

    def CalcObserve(self):
        home = ephem.Observer()
        home.lat = self._gslat
        home.lon = self._gslon
        home.elev = int(self._gselev)
        sat = ephem.readtle(self._satname, self._tle1, self._tle2)
        sat.compute(home)
        sataz = math.degrees(sat.az)
        satalt = math.degrees(sat.alt)
        c = 299792458
        satfreq = float(self._frequency) * self.dopplershift(c, sat.range_velocity)
        risetime=ephem.localtime(sat.rise_time)
        settime=ephem.localtime(sat.set_time)
        return sataz, satalt, satfreq,risetime,settime,math.degrees(sat.transit_alt)

