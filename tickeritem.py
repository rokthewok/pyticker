import ansicolors

class TickerItem:
	def __init__( self, d ):
		self.data = d
		self.offset = 0

	def getFormattedData( self ):
		if '+' in self.data:
			result = ansicolors.AnsiColors.FG_GREEN + self.data[self.offset:]
			return result
		elif '-' in self.data:
			result = ansicolors.AnsiColors.FG_RED + self.data[self.offset:]
			return result
		else:
			result = ansicolors.AnsiColors.FG_WHITE + self.data[self.offset:]
			return result
	
	def incrementOffset( self ):
		self.offset = self.offset + 1

	def isFedThrough( self ):
		if self.offset >= len( self.data ):
			return True
		else:
			return False
