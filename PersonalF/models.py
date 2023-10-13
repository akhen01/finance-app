from django.db import models

#from django.contrib.auth.models import User

# Create your models here.
class incometype(models.Model):
    name = models.CharField(max_length= 64)

    def __str__(self):
        return self.name
    
class budgettype(models.Model):
    name = models.CharField(max_length= 64)

    def __str__(self):
        return self.name
    
class income(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    Itype = models.ForeignKey(incometype, on_delete=models.CASCADE)
    #made_by = models.ForeignKey(User, on_delete=models.CASCADE)

class budget(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    Itype = models.ForeignKey(budgettype, on_delete=models.CASCADE)
    #made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def total(self):
        return sum(i for i in self.amount.all())

class expence(models.Model):
    amount = models.IntegerField()
    Itype = models.ForeignKey(budgettype, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Itype

    def total(self):
        return sum(i for i in self.amount.all())


