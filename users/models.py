from django.db import models
from inventory.models import Inventory

class Users(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=13)
  inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
  
  class Meta:
    db_table="users"