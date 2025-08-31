from django.contrib import admin
from .models import subscription,subscriptionOrder,Converstations,Messages
# Register your models here.

models_list = [subscription,subscriptionOrder,Converstations,Messages]

admin.site.register(models_list)