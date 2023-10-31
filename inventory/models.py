from django.db import models
from products.models import Products

class Inventory(models.Model):
  id = models.AutoField(primary_key=True)
  product = models.ForeignKey(Products, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  
  class Meta:
    db_table="inventory"
    indexes = [
      models.Index(fields=["product_id"], name="product_id_idx"),
    ]