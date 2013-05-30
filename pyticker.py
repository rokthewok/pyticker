#! /usr/bin/python3

import os, urllib.request, time

f = urllib.request.urlopen( "http://download.finance.yahoo.com/d/quotes.csv?s=YHOO+GOOG&f=sl1d1t1c1ohgv&e=.csv" )

#for line in f:
#	print( line )

feed = f.read().decode( "utf-8" ).replace( ',', ' ' ).replace( '\r\n', ' | ' )

os.popen( 'clear', 'w' )
while True:
	rows, columns = os.popen( 'stty size', 'r' ).read().split()
	
	startChar = feed[:1]
	feed = feed[1:]
	feed = feed + startChar
	truncFeed = feed[:int( columns )]
#print( feed.replace( '\r\n', ' | ' ) )
	print( truncFeed )
	time.sleep( 0.3 );
	os.popen( 'clear', 'w' )
