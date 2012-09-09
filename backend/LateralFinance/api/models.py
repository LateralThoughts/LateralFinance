from django.db import models


class Currency(models.Model):
	name = models.CharField(max_length=500)
	symbol = models.CharField(max_length=5)

	def __unicode__(self):
		return "%s (%s)" % (self.name, self.symbol)


class Market(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name


class Company(models.Model):
	full_name = models.CharField(max_length=500)
	symbol = models.CharField(max_length=5)
	market = models.ForeignKey(Market)
	trading_currency = models.ForeignKey(Currency)
	isin = models.CharField(max_length=20)

	def __unicode__(self):
		return "%s (%s)" % (self.full_name, self.symbol)

class Quote(models.Model):
	company = models.ForeignKey(Company)
	created_at = models.DateField()
	open = models.FloatField()
	high = models.FloatField()
	close = models.FloatField()
	low = models.FloatField()
	volume = models.FloatField()