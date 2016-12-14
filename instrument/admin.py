from django.contrib import admin
from .models import Instruments, Order

# Register your models here.
admin.site.register(Instruments)
admin.site.register(Order)
