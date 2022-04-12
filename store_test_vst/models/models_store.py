from django.db import models
from vstutils.models import BModel


class Property(BModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    class Meta:
        default_related_name = "property"
        _detail_fields = [
            'id',
            'name',
            'description'
        ]


class Item(BModel):
    cost_types = (('RUB', 'RUB'),
                  ('USD', 'USD'),
                  ('EUR', 'EUR'))
    name = models.CharField(max_length=256)
    cost = models.IntegerField(default=0)
    cost_type = models.CharField(max_length=50,
                                 choices=cost_types,
                                 default='RUB')
    description = models.CharField(max_length=512)
    properties = models.ManyToManyField(Property)
    image = models.ImageField()
    _translate_model = 'Item'

    class Meta:
        # create nested views from models
        _nested = {
            'properties': {
                'allow_append': True,
                'model': Property
            }
        }
