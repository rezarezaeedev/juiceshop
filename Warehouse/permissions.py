from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    message = 'Just superusers can be see.'

    def has_permission(self, request, view):
        super_result = super().has_permission(request, view)
        if request.method == 'POST':
            if request.user.is_superuser:
                return True
            return False
        return super_result
