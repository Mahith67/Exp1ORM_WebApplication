from django.db import models
from django.contrib import admin

class Order(models.Model):
    order_id = models.IntegerField(help_text="Enter order ID")
    customer_name = models.CharField(max_length=100, help_text="Enter customer name")
    total_amount=models.IntegerField(help_text="Enter Total Amount")
    order_date = models.DateTimeField(help_text="Enter order date")
    status=models.CharField(help_text="Enter Order Status")

class OrderAdmin(admin.ModelAdmin):
    list_display=['order_id','customer_name','order_date','total_amount','status']


