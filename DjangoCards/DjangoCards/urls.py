
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cards', include('loyaltycard.urls')),
    path('admin/', admin.site.urls),
]
