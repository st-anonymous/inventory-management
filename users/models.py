from django.db import models

class Users(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	phone = models.CharField(max_length=13)
  
	class Meta:
		db_table="users"