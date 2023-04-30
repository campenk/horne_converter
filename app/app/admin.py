from django.contrib import admin
from .models import Item, ItemCategory, MeasurementType

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(MeasurementType)


