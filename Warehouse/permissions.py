from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    message = 'Just superusers can be see.'

    def has_permission(self, request, view):
        if request.method in ['POST', "DELETE", "PUT", "PATCH"]:
            if request.user.is_superuser:
                return True
            return False
        return super().has_permission(request, view)
