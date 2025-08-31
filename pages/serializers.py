from rest_framework import serializers

from .models import subscription, Converstations , Messages, subscriptionOrder

class SubSerializers(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = "__all__"

class SubOrderSerializers(serializers.ModelSerializer):
    plan = serializers.PrimaryKeyRelatedField(queryset=subscription.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # we’ll set from request.user in view
    class Meta:
        model = subscriptionOrder
    
        fields = [
            "id", "user", "plan", "stripe_subscription_id",
            "status", "current_period_end", "created_at", "updated_at",
        ]
        read_only_fields = ["created_at","updated_at"]


    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

class MessagesSerializers(serializers.ModelSerializer):
    role_display = serializers.CharField(source="get_role_display", read_only=True)
    class Meta:
        model = Messages
        fields = ["id", "role", "role_display", "content", "created_at"]

class ConverstationsSerializer(serializers.ModelSerializer):
    messages = MessagesSerializers(many=True, read_only=True)

    class Meta:
        model = Converstations
        fields = ["id", "title", "created_at", "updated_at", "messages"]
