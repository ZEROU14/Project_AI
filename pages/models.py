from django.db import models

# Create your models here.
class subscription(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    local_price = models.DecimalField(decimal_places=2,max_digits=6)
    stripe_price_id = models.CharField(max_length=200 , unique=True)


# class subscriptionOrder(models.Model)
