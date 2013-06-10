import tickeritem

def formatFeed( feed ):
	return feed.read().decode( "utf-8" ).replace( ',', ' ' ).replace( '\r\n', ' | ' )

def updateList( tickerList, feed ):
	splitFeed = feed.split( '|' )

	for item in tickerList:
		if item.isFedThrough():
			tickerList.remove( item )

	for item in splitFeed:
		tickerList.append( tickeritem.TickerItem( item ) )
