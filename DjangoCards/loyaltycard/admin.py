from django.contrib import admin

# Register your models here.

from .models import Card, Purchase

admin.site.register(Card)
admin.site.register(Purchase)

