from rest_framework import permissions

class IsStudent(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.name=='Student'
    
class IsFaculty(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.name=='Faculty'
        