from typing import Required
from rest_framework import serializers
from users.models import Users
from .models import Inventory

class InventorySerializer(serializers.Serializer):
	id = serializers.CharField(required=True, max_length=10)
	user = serializers.PrimaryKeyRelatedField(required=True, read_only=False, queryset=Users.objects.all())
	product = serializers.CharField(required=True, max_length=50)
	quantity = serializers.IntegerField(required=True)
	type = serializers.ChoiceField({"add": "add", "remove": "remove"})

	class Meta:
		model = Inventory
		fields = ['id', 'user', 'product', 'quantity']
  
	def validate_quantity(self, value):
		if value < 0:
			raise serializers.ValidationError("Quantity is more than that in inventory")
 
 
class GetInventorySerializer(serializers.Serializer):
  id = serializers.CharField(max_length=10, allow_null=True, required=False)
  user = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Users.objects.all())
  product = serializers.CharField(max_length=50, allow_null=True, required=False)
  
  class Meta:
    model = Inventory
    fields = ['id', 'user', 'product']