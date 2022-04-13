from rest_framework.permissions import IsAuthenticated


class ItemsHandlingPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method.lower() == 'get':
            return True
        else:
            return super().has_permission(request, view)
