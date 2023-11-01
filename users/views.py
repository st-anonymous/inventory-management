from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UsersSerializer
import json, random

def generate_user_id():
  prefix = 'uid'
  random_number = random.randint(1, 9999999)
  formatted_number = f"{random_number:07d}"
  user_id = f"{prefix}{formatted_number}"
  if Users.objects.filter(id = user_id).exists():
    user_id = generate_user_id()
  return user_id

class createUser(APIView):
  def post(self, request):
    data = request.body
    data = json.loads(data)
    user_id = generate_user_id()
    name = data['name']
    email = data['email']
    phone = data['phone']
    serializer = UsersSerializer(data={
      'id': user_id,
      'name': name,
      'email': email,
      'phone': phone
    })
    if serializer.is_valid():
      Users.objects.create(id=user_id, name=name, email=email, phone=phone)
      return Response({"message": f"New User Created for user_id {user_id}."}, status = status.HTTP_201_CREATED)
    return Response({"message": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

class userDetails(APIView):
  def get(self, request, user_id):
    if Users.objects.filter(id = user_id).exists():
      data = Users.objects.get(id = user_id)
      return Response({"message": f"User fetched for user_id {user_id}.", "name": f"{data.name}", "email": f"{data.email}", "phone": f"{data.phone}"}, status=status.HTTP_200_OK)
    return Response({"message": f"User could not be fetched for user_id {user_id}."}, status=status.HTTP_404_NOT_FOUND)