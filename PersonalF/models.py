from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

#from django.contrib.auth.models import User

# Create your models here.

Cnames = [
        ("Fun" ,"Fun" ),                    # includes drinking, eating, dates, nightout
        ("Apparel", "Apparel"),             # clothes, shoes, glasses, jewelry and other warable products
        ("Grocery", "Grocery"),             # eatable products
        ("Cleaning", "Cleaning"),           # products used for cleaning
        ("Electronics", "Electronics"),     # laptops, phones etc..
        ("Furniture", "Furniture"),         # beds, sofas etc...
        ("Rent", "Rent"),
        ("Bills", "Bills")
    ]
    
class Money(models.Model):
    types = [
        ("income","income"),
        ("expence", "expence")
    ]
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    discription = models.CharField(max_length=50, blank=False, null=False)
    Mtype = models.CharField(max_length=50, choices=types, blank=False, null=False)
    catagory_name = models.CharField(max_length=50, choices=Cnames, default="Rent", blank=True, null=True)
    amount = models.IntegerField(blank=False, null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.discription

class Budget(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    budget_type = models.CharField(max_length=50, choices=Cnames, default="Rent", blank=False, null=False)
    for_month = models.DateField(default=timezone.now(), blank=False, null=False)

    def __str__(self):
        return self.budget_type


# need to include all the data in one model 
