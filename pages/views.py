from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from django.db.models import Prefetch

from .permissions import IsOwner
from .serializers import *
from .models import *
# Create your views here.



class SubViewSet(viewsets.ModelViewSet):
    serializer_class = SubSerializers
    queryset = subscription.objects.all().order_by("id")
    permission_classes = permissions.IsAdminUser

class SubOrderViewSrt(viewsets.ModelViewSet):
    serializer_class = SubOrderSerializers
    permission_classes = [IsOwner,permissions.IsAuthenticated]

    def get_queryset(self):
        return(
            subscriptionOrder.objects
            .select_related('plan','user')
            .filter(user=self.request.user)
            .order_by('created_at')
        )

    @action(detail=False, methods=["get"], url_path="active")
    def active(self, request):
        obj = self.get_queryset().filter(status="active").first()
        ser = self.get_serializer(obj)
        return Response(ser.data if obj else None)

    @action(detail=False, methods=["post"], url_path="cancel")
    def cancel(self, request):
    
        obj = self.get_queryset().filter(status="active").first()
        if not obj:
            return Response({"detail": "No active subscription."}, status=400)
        
        obj.status = "inactive"
        obj.current_period_end = now()
        obj.save(update_fields=["status", "current_period_end", "updated_at"])
        return Response(self.get_serializer(obj).data)



class ConverstationViewSet(viewsets.ModelViewSet):
    serializer_class = ConverstationsSerializer
    pagination_class = [IsOwner,permissions.IsAuthenticated]
    
    def get_queryset(self):
        return (
            Converstations.objects
            .filter(user=self.request.user)
            .prefetch_related('messages',)
        ).order_by('-created-at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def messages(self, request, pk=None):
        conv = self.get_object()
        ser = MessageCreateSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        msg = Message.objects.create(conversation=conv, **ser.validated_data)
        return Response(MessageSerializer(msg).data, status=201)
    
class MessageCreateSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=Messages.ROLE_CHOICES)
    content = serializers.CharField()


class MessagesViewSet(viewsets.ModelViewSet):
    serializer_class = MessagesSerializers
    queryset = Messages.objects.all()