from rest_framework import permissions

class HasAdminRolePermission(permissions.BasePermission):
    message = "You have to have admin role permission to perform this action"

    def has_permission(self, request, view):
        return request.user.role == 'admin'

class HasUserRolePermission(permissions.BasePermission):
    message = "You have to have user role permission  to perform this action"

    def has_permission(self, request, view):
        return request.user.role == 'user'