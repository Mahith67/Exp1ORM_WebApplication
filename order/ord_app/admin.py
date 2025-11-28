from django.contrib import admin
from .models import Order,OrderAdmin
# Register your models here.
admin.site.register(Order,OrderAdmin)