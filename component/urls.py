from rest_framework import routers

from .views import ComponentsViewSet


routers = routers.DefaultRouter()


routers.register("Components",ComponentsViewSet , basename="component")

urlpatterns = routers.urls
