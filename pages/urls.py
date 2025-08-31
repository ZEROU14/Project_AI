from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubViewSet, SubOrderViewSrt,ConverstationViewSet

router = DefaultRouter()
router.register(r"subscriptions", SubViewSet, basename="subscription")
router.register(r"subscription-orders", SubOrderViewSrt, basename="subscription-order")
router.register(r"conversations", ConverstationViewSet, basename="conversation")

urlpatterns = [
    path("api/", include(router.urls)),
]