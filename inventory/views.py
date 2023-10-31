from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.models import Users
from .serializers import InventorySerializer
from .models import Inventory
import json, random


def generate_inventory_id():
  prefix = 'iid'
  random_number = random.randint(1, 9999999)
  formatted_number = f"{random_number:07d}"
  inventory_id = f"{prefix}{formatted_number}"
  if Inventory.objects.filter(id = inventory_id).exists():
    inventory_id = generate_inventory_id()
  return inventory_id

class inventoryItems(APIView):
  def post(self, request):
    data = request.body
    data = json.loads(data)
    user = Users.objects.get(id=data['user'])
    product = data['product']
    quantity = data['quantity']
    
    if Inventory.objects.filter(user=user).filter(product=product).exists():
      quantity += Inventory.objects.get(user=user, product=product).quantity
      inventory_id = Inventory.objects.get(user=user, product=product).id
      create = False
    else:
      inventory_id = generate_inventory_id()
      create = True
      
    serializer = InventorySerializer(data={
      'id': inventory_id,
      'user': user.pk,
      'product': product,
      'quantity': quantity
    })
    if serializer.is_valid():
      if create:
        Inventory.objects.create(id=inventory_id,user=user,product=product,quantity=quantity)
      else:
        Inventory.objects.filter(id=inventory_id).update(quantity=quantity)
      return Response({"message": "Successfully saved"}, status=status.HTTP_201_CREATED)
    return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    