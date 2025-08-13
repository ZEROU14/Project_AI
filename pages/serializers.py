from rest_framework import serializers

from .models import subscription, Converstations , Messages

class SubSerializers(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = "__all__"


class ConverstationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Converstations
        fields = "__all__"

class MessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'