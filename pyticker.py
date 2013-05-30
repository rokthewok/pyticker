#! /usr/bin/python3

import os, urllib.request, time
import ansicolors
import sys

def printFeed( feed, columns ):
	splitFeed = feed.split( '|' )

	newFeed = ''
	for item in splitFeed:
		if '+' in item:
			newFeed = newFeed + ansicolors.AnsiColors.FG_GREEN + item + ansicolors.AnsiColors.FG_WHITE + '|'
		elif '-' in item:
			newFeed = newFeed + ansicolors.AnsiColors.FG_RED + item + ansicolors.AnsiColors.FG_WHITE + '|'
		else:
			newFeed = newFeed + ansicolors.AnsiColors.FG_BLACK + item + ansicolors.AnsiColors.FG_WHITE + '|'
	
	print( newFeed[:columns + 22] );

params = ''
if len( sys.argv ) > 1:
	for arg in sys.argv:
		params = params + arg + '+'
	
	params = params[:len( params ) - 1]
else:
	params = 'GOOG+MSFT'

url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + params + "&f=sl1d1t1c1ohgv&e=.csv" 
f = urllib.request.urlopen( url )

feed = f.read().decode( "utf-8" ).replace( ',', ' ' ).replace( '\r\n', ' | ' )

os.popen( 'clear', 'w' )
while True:
	rows, columns = os.popen( 'stty size', 'r' ).read().split()
	
	startChar = feed[:1]
	feed = feed[1:]
	feed = feed + startChar
	truncFeed = feed[:int( columns )]

	printFeed( truncFeed, int( columns ) )	
	time.sleep( 0.3 );
#	if count == 30:
#		f = 
	os.popen( 'clear', 'w' )
