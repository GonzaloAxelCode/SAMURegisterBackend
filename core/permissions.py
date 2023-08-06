from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario es un administrador
        if not request.user.is_authenticated:
            return False

        if request.user.desactivate_account:
            return False

        return request.user.has_perm('core.user')
