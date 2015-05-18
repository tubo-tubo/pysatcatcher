# coding: utf-8
import radio

class Radio(object):
	
	def __init__(self,connect):
		self.connect = connect
		#print(self.typ)
		#print(self.connect)

	def seek(self,typ,modeSubMain,modeCWFM):
		#ic910 = radio.Radio("IC910","Sub","CW")
		self.ic910 = radio.Radio(typ,modeSubMain,modeCWFM)
		#ic910.changefreq(437.485)

	def change_freq(self,freq):
		self.ic910.changefreq(freq)
		print(self.ceurrentfreq)

	def close(self):
		self.ic910.close()