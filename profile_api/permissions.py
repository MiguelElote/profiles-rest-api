from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        #obj is the object they want to access.
        #request.user is the authenticated user, which Django attaches to the request.
        #If the id's match, that means the user is updating the object for their id.
        return obj.id == request.user.id
