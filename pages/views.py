from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *
# Create your views here.

class SubViewSet(ModelViewSet):
    serializer_class = SubSerializers
    queryset = subscription.objects.all()


class ConverstationViewSet(ModelViewSet):
    serializer_class = ConverstationsSerializer
    queryset = Converstations.objects.all()


class MessagesViewSet(ModelViewSet):
    serializer_class = MessagesSerializers
    queryset = Messages.objects.all()