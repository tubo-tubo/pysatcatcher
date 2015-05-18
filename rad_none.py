# coding: utf-8
import radio

class Radio(object):
	
	def __init__(self,connect):
		self.connect = connect
		#print(self.typ)
		#print(self.connect)

	def seek(self,typ,modeSubMain,modeCWFM):
		self.ic910 = radio.Radio(typ,modeSubMain,modeCWFM)
		#self.ic910 = radio.Radio(typ,modeSubMain,modeCWFM)
		return True

	def change_freq(self,freq):
		self.frequency = freq
		#self.ic910.changefreq(freq)
		return self.frequency

	def close(self):
		#self.ic910.close()
		return True