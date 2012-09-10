from django.http import HttpResponse
from models import Company
import json
from django.shortcuts import get_object_or_404

def home(request):
	""" Index page """
	companies = Company.objects.all()
	return HttpResponse(
		json.dumps(
			[company.to_dict() for company in companies]
		), mimetype="application/json")


def autocomplete(request):
	from haystack.query import SearchQuerySet as sqs
	results = sqs().autocomplete(content_auto = request.GET.get('q', None))
	return HttpResponse(json.dumps(
			[{
				'text' : result.text,
				'symbol' : result.symbol,
				'pk' : result.object.pk,
			} for result in results]
		), mimetype="application/json")


def quotes(request):
	""" Returns Quotes on a period until today """
	requested_id = request.GET.get('id', None)
	company = get_object_or_404(Company, pk=requested_id)
	quotes = company.quotes.all()
	if len(quotes) == 0:
		try:
			from api.utils import load_data_from_company
			quotes = load_data_from_company(company)
		except Exception, e:
			print e
	return HttpResponse(json.dumps(
    		{
    			'company' : company.to_dict(),
    			'quotes' : [{
    				'id' : quote.pk,
    				'date' : str(quote.created_at),
    				'open' : quote.open,
    				'high' : quote.high,
    				'low' : quote.low,
    				'close' : quote.close,
    				'volume' : quote.volume
    			} for quote in quotes],
    		}
    	), mimetype="application/json")