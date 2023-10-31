from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include("users.urls")),
    path('inventory/', include("inventory.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
