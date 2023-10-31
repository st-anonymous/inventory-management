from rest_framework import serializers
from users.models import Users
from .models import Inventory

class InventorySerializer(serializers.Serializer):
	id = serializers.CharField(required=True, max_length=8)
	user = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Users.objects.all())
	product = serializers.CharField(required=True, max_length=50)
	quantity = serializers.IntegerField(required=True)

	class Meta:
		model = Inventory
		fields = ['id', 'user', 'product', 'quantity']