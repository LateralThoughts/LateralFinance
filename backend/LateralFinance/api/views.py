from django.http import HttpResponse
from models import Company
import json

def home(request):
	""" Index page """
	companies = Company.objects.all()
	return HttpResponse(
		json.dumps(
			[{
				'id' : company.pk,
				'symbol' : company.symbol,
				'name' : company.full_name,
				'currency' : company.trading_currency.symbol,
				'market' : company.market.name,
			} for company in companies]
		), mimetype="application/json")