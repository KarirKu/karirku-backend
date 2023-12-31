from rest_framework import permissions

class IsCurrentUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
    
class IsAlumniUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user and request.user.user_type == 'alumni'
        except:
            return False

class IsMahasiswaUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user and request.user.user_type == 'mahasiswa'
        except:
            return False
        