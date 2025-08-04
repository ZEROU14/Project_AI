from rest_framework import serializers

from .models import subscription

class SubSerializers(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = "__all__"
