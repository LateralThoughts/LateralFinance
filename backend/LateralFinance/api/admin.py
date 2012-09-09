from django.contrib import admin
from api.models import Company, Currency, Market, Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['company', 'created_at', 'open', 'high', 'low', 'close', 'volume']
admin.site.register(Quote, QuoteAdmin)
