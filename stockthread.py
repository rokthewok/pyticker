import urllib
import os
import threading
import time
import stockutils

class StockThread(threading.Thread):
	
	def __init__(self, tl, url):
		super().__init__()
		self.count = 0
		self.tickerList = tl
		self.url = url
		self.daemon = True

	def run(self):
		while( True ):
			if( self.count == 10 ):
				self.count = 0
				print( "hello!" )
				f = urllib.request.urlopen( self.url )
				feed = stockutils.formatFeed( f )
				stockutils.updateList( self.tickerList, feed )
			
			time.sleep(1)
			self.count = self.count + 1
