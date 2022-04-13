from vstutils.api.decorators import nested_view
from vstutils.api.permissions import SuperUserPermission

from .permissions import ItemsHandlingPermission
from .serializers import ItemSerializer, PropertyCustomSerializer
from .models import Item, Property


class PropertyViewSet(Property.generated_view):
    serializer_class_one = PropertyCustomSerializer
    permission_classes = (ItemsHandlingPermission,)


@nested_view('properties',
             manager_name='properties',
             allow_append=True,
             methods=['post', 'get', 'put', 'patch', 'delete'],
             view=PropertyViewSet)
class ItemViewSet(Item.generated_view):
    serializer_class = ItemSerializer
    permission_classes = (ItemsHandlingPermission,)
