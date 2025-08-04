from rest_framework import routers
from .views import SubViewSet


routers = routers.DefaultRouter()


routers.register("Subscription" , SubViewSet,basename='sub')


urlpatterns = routers.urls


