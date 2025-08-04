from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *
# Create your views here.

class SubViewSet(ModelViewSet):
    serializer_class = SubSerializers
    queryset = subscription.objects.all()
