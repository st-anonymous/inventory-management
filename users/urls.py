from django.urls import path
from .views import createUser, userDetails

urlpatterns = [
  path("create", createUser.as_view()),
  path("details/<str:user_id>", userDetails.as_view()),
]