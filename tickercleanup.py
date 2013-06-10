import threading
import os
import sys

class CleanUp:
	
	def __init__( self, thread ):
		self.thread = thread
	
	def clean_up( self, signum, frame ):
		os.popen( 'clear', 'w' )
		os.popen( 'tput cnorm', 'w' )
		sys.exit( 0 )
