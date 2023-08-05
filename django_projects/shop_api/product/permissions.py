from rest_framework.permissions import BasePermission

from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return request.user == obj.owner

# class IsAuthorOrAdminOrOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser:
#             return True
#         if request.user == obj.post.owner:
#             return True
#         return request.user == obj.owner
