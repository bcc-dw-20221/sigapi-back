from rest_framework import permissions
from SIGAPI_rest.models import Professor 
from django.contrib.auth import get_user_model
from django.contrib import auth


class IsAdminOrReadOnly(permissions.BasePermission):

    edit_methods = ("GET", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
class IsProfessorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        user = get_user_model().objects.filter(pk=request.user.id)
        user = Professor.objects.filter(user=3)
        print("este e o user:",user)
        
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
        if request.user.is_authenticated:
            if Professor.objects.filter(user=request.user.id):
                return True