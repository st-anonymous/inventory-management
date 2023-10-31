from django.urls import path
from .views import inventoryItems


urlpatterns = [
  path("", inventoryItems.as_view()),
]