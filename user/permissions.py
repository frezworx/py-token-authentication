from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
        ):
            return True
        return request.user and request.user.is_staff
