import datetime
from haystack import indexes
from models import Company


class StockIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    symbol = indexes.CharField(model_attr='symbol', boost=1.125)

    content_auto = indexes.EdgeNgramField(model_attr = 'full_name')
    def get_model(self):
        return Company
