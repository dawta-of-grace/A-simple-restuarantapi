from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default= True)

    def __str__(self):
        return self.name
    
    
class Order(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     items = models.ManyToManyField('menuItem')
     ordered_at = models.DateTimeField(auto_now_add=True)


     def __str__(self):
         return f"order {self.id} by {self.user.username}"

