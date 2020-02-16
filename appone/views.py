from django.shortcuts import render
from appone.serializers import *
from appone.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission,IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly


#def Testops():
    #return "Hello World"
def test():
    pass

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return int(request.data['stage']) > 30

    def has_object_permission(self, request, view, obj):
        return True


class StudentOps(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = StudInfo.objects.all()
    serializer_class = StudentSer


class AddressOps(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Address.objects.all()
    serializer_class = AddressSer

    def get_permissions(self):
        if self.action == "destroy":
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()
