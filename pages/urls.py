from rest_framework import routers
from .views import SubViewSet , ConverstationViewSet,MessagesViewSet


routers = routers.DefaultRouter()


routers.register("Subscription" , SubViewSet,basename='sub')
routers.register("Converstations", ConverstationViewSet,basename='Conv')
routers.register("Converstations", MessagesViewSet,basename='messages')



urlpatterns = routers.urls


