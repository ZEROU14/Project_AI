from django.db import models
from django.conf import settings 

# Create your models here.
class subscription(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    local_price = models.DecimalField(decimal_places=2,max_digits=6)
    stripe_price_id = models.CharField(max_length=200 , unique=True)


class subscriptionOrder(models.Model):
    STATUS_CHOICES = [
        ('activ','ACTIVE'),
        ('inactive',"InACTIVE"),
        
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscription'
    )

    plan = models.ForeignKey(subscription,on_delete=models.SET_NULL)
    stripe_subscription_id = models.CharField(max_length=255,unique=True)
    status = models.CharField(choices=STATUS_CHOICES,default=STATUS_CHOICES[1])
    current_period_end = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.plan.title} - {self.status}'


class Converstations(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_NODEL,
        on_delete=models.CASCADE,
        related_name='converstations'
    )
    title = models.CharField(max_length=255,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upadeted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return [
            {"role": msg.role, "content" : msg.content}
            for msg in self.messages.order_by("created_at")
        ]
    

class Messages(models.Model):
    ROLE_CHOICES = [
        ('system','System'),
        ('user', "User"),
        ('assistant', "Assistant"),
        ('tool',"Tool") 
    ]

    converstations = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='messages',
    )
    role = models.CharField(max_length=50 ,choices=ROLE_CHOICES)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.role} : {self.content[:50]}"