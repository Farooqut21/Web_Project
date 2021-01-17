from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name =models.CharField(max_length=20,blank=False,null=False)
    last_name= models.CharField(max_length=20, blank=False, null=False)
    city=models.CharField(max_length=20 ,blank=True,null=True)
    country = models.CharField(max_length=25,blank=True,null=True)
    zip=models.IntegerField(blank=True,null=True)

    pass
