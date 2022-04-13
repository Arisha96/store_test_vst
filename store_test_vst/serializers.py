from . import models as models


class PropertyCustomSerializer(models.Property.generated_view.serializer_class):

    class Meta:
        model = models.Property
        fields = ('id',
                  'name',
                  'description')


class ItemSerializer(models.Item.generated_view.serializer_class):
    properties = PropertyCustomSerializer(many=True)

    class Meta:
        model = models.Item
        fields = ('id',
                  'name',
                  'description',
                  'cost',
                  'cost_type',
                  'image',
                  'properties')


