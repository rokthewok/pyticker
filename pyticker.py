#! /usr/bin/python3

import os, urllib.request, time
import ansicolors
import sys
import tickeritem
import signal
import stockthread
import tickercleanup
from stockutils import formatFeed, updateList

def printFeed( tickerList, columns ):
	newFeed = ''
	count = 0
	for item in tickerList:
		newFeed = newFeed + item.getFormattedData() + ansicolors.AnsiColors.FG_WHITE + '|'
		count = count + 1
		if count > 10:
			break

	count = count - 1
	tickerList[0].incrementOffset()

	print( ansicolors.AnsiColors.BG_BLACK + newFeed[:columns + ( count * 2 )] );
	#os.popen( 'echo -e "\r\033[K"', 'w' )
	
	cleanList( tickerList )

def cleanList( tickerList ):
	for item in tickerList:
		if item.isFedThrough():
			tickerList.remove( item )

def cleanUp( signal, frame ):
	os.popen( 'clear', 'w' )
	os.popen( 'tput cnorm', 'w' )
	sys.exit( 0 )

def main():
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

	stockThread = stockthread.StockThread( tickerList, url )
	cu = tickercleanup.CleanUp( stockThread )
	signal.signal( signal.SIGINT, cu.clean_up )

	stockThread.start()

	os.popen( 'clear', 'w' )
	count = 0
	while True:
		rows, columns = os.popen( 'stty size', 'r' ).read().split()

		printFeed( tickerList, int( columns ) )	
		time.sleep( 0.2 );
		
		os.popen( 'clear', 'w' )
		count = count + 1
	

if __name__ == "__main__":
	main()
