from csv import DictReader
from models import *

CUR_REF = {
	'EUR' : 'Euro',
	'GBP' : 'Great Britain Pound',
	'USD' : 'US Dollar',
	'CHF' : 'Franc Suisse',
	'CZK' : "Couronne CZK",
	'NOK' : 'Couronne Norvegienne',
	'SEK' : 'Swedish Krohn',
	'HUF' : 'Hungarian Francs',
	'DKK' : 'Monnaie de raciste',
}
def load_all_symbols():
	"""
	{'Volume': '2144', 
		'Time Zone': 'CET', 
		'Last': '36.99', 
		'Name': '1000MERCIS', 
		'Symbol': 'ALMIL', 
		'High': '37.00', 
		'Low': '36.86', 
		'Last Date/Time': '07/09/2012 17:07', 
		'Trading Currency': 'EUR', 
		'ISIN': 'FR0010285965', 
		'Open': '36.86', 
		'Market': 'NYSE Alternext Paris', 
		'Turnover': '79312.41'}
	"""
	flux = DictReader(open('NYX_Equities_EU_2012-09-09.csv'), delimiter=";")
	for line in flux:
		currency = line['Trading Currency']
		trading_currency, created = Currency.objects.get_or_create(
			name=CUR_REF[currency], 
			symbol=currency)
		market, created = Market.objects.get_or_create(
			name = line['Market'])
		symbol, created = Company.objects.get_or_create(
			full_name = line['Name'],
			symbol = line['Symbol'],
			market = market,
			trading_currency = trading_currency,
			isin = line['ISIN'])

import requests
YAHOO_URL = "http://ichart.finance.yahoo.com/table.csv?s=%s"
from datetime import datetime
def load_data_from_company(company):
	"""
	Load data from yahoo finance to store all quotes
	Date,Open,High,Low,Close,Volume,Adj Close
	2012-09-07,678.05,682.48,675.77,680.44,11756500,680.44
	"""
	url =YAHOO_URL % company.symbol
	print "URL : %s" % url
	data = requests.get(url)
	flux = DictReader(data.content.split("\n"), delimiter=",")
	index = 0
	for line in flux:
		index += 1
		if index % 100 == 0:
			print "Treating line %s" % index
		quote = Quote()
		quote.company = company
		quote.created_at = datetime.strptime(line['Date'], "%Y-%m-%d")
		quote.open =line['Open']
		quote.high =line['High']
		quote.low = line['Low']
		quote.close = line['Adj Close']
		quote.volume = line['Volume']

		quote.save()















