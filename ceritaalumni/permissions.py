from rest_framework import permissions
from user.models import User

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            # Write permissions are only allowed to the owner of the snippet.
            return obj.alumni == User.objects.get(id=request.user.id)
        except:
            return False