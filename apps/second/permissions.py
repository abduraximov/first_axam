from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return obj.review_user == request.user or request.user.is_staff
        if request.user == obj.user and request.method in ["GET", "PUT", "PATCH"]:
            return True
        elif request.user.is_staff:
            return True
        return False
