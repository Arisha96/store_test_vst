from vstutils.api import decorators as deco
from rest_framework.permissions import AllowAny
from .serializers import ItemSerializer
from .models import Item, Property


class PropertyViewSet(Property.generated_view):
    permission_classes = (AllowAny,)


@deco.nested_view('properties',
                  manager_name='properties',
                  methods=['post', 'get', 'put', 'patch', 'delete'],
                  view=PropertyViewSet)
class ItemViewSet(Item.generated_view):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
