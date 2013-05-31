PyTicker
--------

A terminal stock ticker. Invoke using
	python3 pyticker.py [SYMBOLS]
where [SYMBOLS] are the stock symbols, seperated by spaces, you wish to monitor.

Output is seperated by pipes, with the fields of each item being the symbol, last trade time, last trade value, point and percentage change, and volume.

Alternatively, the script may be invoked by first calling
	chmod +x pyticker.py
Then from there on executing the script with
	./pyticker.py [SYMBOLS]
