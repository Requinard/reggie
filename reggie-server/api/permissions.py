from rest_framework import permissions

import users.models
import registration.models


class ProfileEditPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: users.models.ProfileModel):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

