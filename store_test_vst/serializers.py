from . import models as models


class ItemSerializer(models.Item.generated_view.serializer_class):
    properties = models.Property.generated_view.serializer_class(many=True)

    class Meta:
        model = models.Item
        fields = ('id',
                  'name',
                  'description',
                  'cost',
                  'cost_type',
                  'image',
                  'properties')


