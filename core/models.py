from statistics import mode
from django.db import models
from django.contrib.auth.models import User


PriceStatus = (
    ("created", "created"),
    ("deleted", "deleted"),
    ("triggered", "triggered"),
)

class BTCAlert(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    price_status = models.CharField(choices=PriceStatus,max_length=20,default="created")   
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now=True)
    deleted_at= models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user.username
        


