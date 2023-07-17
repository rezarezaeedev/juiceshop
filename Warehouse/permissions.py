from rest_framework import permissions

class IsSuperUser(permissions.IsAdminUser):
    message = 'Just superusers can be see.'

    def has_permission(self, request, view):
        super_result = super().has_permission(request, view)
        if request.user.is_superuser:
            return True
        return False