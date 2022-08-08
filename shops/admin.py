from django.contrib import admin

# Register your models here.

from .models import Plan, Subscription, OrderDetail

admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(OrderDetail)
