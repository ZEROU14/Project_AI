"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
>>>>>>> 79e91d3155515e220788e7cf27b0abaae48a1637
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Sub/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('accounts/', include('allauth.urls')),
    # path('api/auth/social/', include('social_django.urls', namespace='social')),
] + debug_toolbar_urls()
