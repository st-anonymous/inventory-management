from requests import delete
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.models import Users
from .serializers import GetInventorySerializer, InventorySerializer
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
    product = data['product'].lower()
    quantity = data['quantity']
    type = data['type']
    
    if Inventory.objects.filter(user=user, product=product).exists():
      if type == 'add':
        quantity = Inventory.objects.get(user=user, product=product).quantity + quantity
      else:
        quantity = Inventory.objects.get(user=user, product=product).quantity - quantity
      inventory_id = Inventory.objects.get(user=user, product=product).id
      create = False
    else:
      if type == 'remove':
        return Response({"message": "No such product exists"}, status=status.HTTP_404_NOT_FOUND)
      inventory_id = generate_inventory_id()
      create = True
      
    serializer = InventorySerializer(data={
      'id': inventory_id,
      'user': user.pk,
      'product': product,
      'quantity': quantity,
      'type': type
    })
    if serializer.is_valid():
      if create:
        Inventory.objects.create(id=inventory_id,user=user,product=product,quantity=quantity)
      else:
        if quantity == 0:
          Inventory.objects.get(id=inventory_id).delete()
        else:
          Inventory.objects.filter(id=inventory_id).update(quantity=quantity)
      return Response({"message": "Successfully saved"}, status=status.HTTP_201_CREATED)
    return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
  def get(self, request):
    data = request.query_params
    id = data.get('id')
    user_id = data.get('user')
    if not Users.objects.filter(id=user_id).exists():
      return Response({"message": "User doesn't exists"}, status=status.HTTP_404_NOT_FOUND)
    user = Users.objects.get(id=user_id)
    product = data.get('product')
    if Inventory.objects.filter(user=user).exists():
      if product:
        product = product.lower()
        inventory = Inventory.objects.filter(user=user, product=product)
      else:
        inventory = Inventory.objects.filter(user=user)
      inventory_info = {}
      for item in inventory:
        inventory_info[f"{item.product}"] = f"{item.quantity}"
      return Response({"message": "Successfully extracted inventory info", "inventory_info": f"{inventory_info}"}, status=status.HTTP_200_OK)
    return Response({"message": "No Inventory items found for the user"}, status=status.HTTP_404_NOT_FOUND)