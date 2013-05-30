#! /usr/bin/python3

import os, urllib.request

f = urllib.request.urlopen( "http://download.finance.yahoo.com/d/quotes.csv?s=YHOO+GOOG&f=sl1d1t1c1ohgv&e=.csv" )

#for line in f:
#	print( line )

feed = f.read().decode( "utf-8" ).replace( ',', ' ' )
	
print( feed.replace( '\r\n', ' | ' ) )
