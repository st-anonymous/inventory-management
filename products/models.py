from django.db import models

class Products(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=300)
  
  class Meta:
    db_table="products"
    indexes = [
      models.Index(fields=["name"], name="name_idx"),
    ]
