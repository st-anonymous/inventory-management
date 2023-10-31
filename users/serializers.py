from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.Serializer):
	id = serializers.CharField(required=True)
	name = serializers.CharField(required=True, max_length=50)
	email = serializers.EmailField(required=True, max_length=254)
	phone = serializers.CharField(required=True, min_length=13, max_length=13)

	class Meta:
		model = Users
		fields = ['id', 'name', 'email', 'phone']
		
	def validate_phone(self, value):
		if Users.objects.filter(phone = value).exists():
			raise serializers.ValidationError("This Phone number is already registered")
		return value

	def validate_email(self, value):
		if Users.objects.filter(email = value).exists():
			raise serializers.ValidationError("This email is already registered")
		return value

	def validate_user_id(self, value):
		if Users.objects.filter(id = value).exists():
			raise serializers.ValidationError("This user_id is already registered")
		return value

	def create(self,validated_data):
		return Users.objects.create(**validated_data)