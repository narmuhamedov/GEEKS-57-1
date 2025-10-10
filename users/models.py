from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(User):
    GENDER = (
        ('m', 'm'),
        ('f', 'f')
    )
    phone_number = models.CharField(max_length=12,default='+996')
    gender = models.CharField(max_length=100, choices=GENDER, default='m')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    


