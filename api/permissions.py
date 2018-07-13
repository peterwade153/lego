from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Only allow owners of businesses edit and delete
    permissions
    '''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # edit and delete permissions only for business owner
        return obj.owner == request.user