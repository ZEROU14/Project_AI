from django.shortcuts import render
from .models import Components
from .serializers import ComponentsSerializer
# Create your views here.


from rest_framework.viewsets import ModelViewSet


class ComponentsViewSet(ModelViewSet):
    serializer_class = ComponentsSerializer
    queryset = Components.objects.all()

