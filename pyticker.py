#! /usr/bin/python3

import os, urllib.request, time
import ansicolors
import sys
import tickeritem
import signal

def printFeed( tickerList, columns ):
	newFeed = ''
	length = 0
	for item in tickerList:
		newFeed = newFeed + item.getFormattedData() + ansicolors.AnsiColors.FG_WHITE + '|'
		length = length + len( item.getFormattedData() ) - 7
		if( length > columns ):
			break

	tickerList[0].incrementOffset()

	print( newFeed[:columns] );
	
	cleanList( tickerList )

def formatFeed( feed ):
	return feed.read().decode( "utf-8" ).replace( ',', ' ' ).replace( '\r\n', ' | ' )

def cleanList( tickerList ):
	for item in tickerList:
		if item.isFedThrough():
			tickerList.remove( item )

def updateList( tickerList, feed ):
	splitFeed = feed.split( '|' )

	for item in tickerList:
		if item.isFedThrough():
			tickerList.remove( item )

	for item in splitFeed:
		tickerList.append( tickeritem.TickerItem( item ) )

def cleanUp( signal, frame ):
	os.popen( 'clear', 'w' )
	os.popen( 'tput cnorm', 'w' )
	sys.exit( 0 )

def main():
	signal.signal( signal.SIGINT, cleanUp )
	os.popen( 'tput civis', 'w' )

	tickerList = []
	params = ''
	if len( sys.argv ) > 1:
		symbols = sys.argv.remove( sys.argv[0] )
		for arg in sys.argv:
			params = params + arg + '+'
		
		params = params[:len( params ) - 1]
	else:
		params = 'GOOG+MSFT'

	url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + params + "&f=sl1d1t1c1ohgv&e=.csv" 
	f = urllib.request.urlopen( url )

	feed = formatFeed( f )
	updateList( tickerList, feed )

	os.popen( 'clear', 'w' )
	count = 0
	while True:
		rows, columns = os.popen( 'stty size', 'r' ).read().split()

		printFeed( tickerList, int( columns ) )	
		time.sleep( 0.2 );
		if count == 30:
			f = urllib.request.urlopen( url )
			feed = formatFeed( f )
			updateList( tickerList, feed )
			count = 0
		os.popen( 'clear', 'w' )
		count = count + 1
	

if __name__ == "__main__":
	main()
