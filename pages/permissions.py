from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # works for Conversation, SubscriptionOrder which both have `user`
        return getattr(obj, "user_id", None) == request.user.id
