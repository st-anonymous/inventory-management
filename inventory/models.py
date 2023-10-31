from django.db import models
from users.models import Users

class Inventory(models.Model):
  id = models.CharField(primary_key=True, max_length=10)
  user = models.ForeignKey(Users, on_delete=models.CASCADE)
  product = models.CharField(max_length=50)
  quantity = models.IntegerField()
  
  class Meta:
    db_table="inventory"
    indexes = [
      models.Index(fields=["user"], name="user_idx"),
      models.Index(fields=["product"], name="product_idx"),
    ]