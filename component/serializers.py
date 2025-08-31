from rest_framework import serializers
 
from .models import Components

class ComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Components
        fields = "__all__"