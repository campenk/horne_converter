from django.db import models


class MeasurementType(models.Model):
    measurementType = models.CharField(max_length=255)

    def __str__(self):
        return self.measurementType


class ItemCategory(models.Model):
    itemCategory = models.CharField(max_length=255)

    def __str__(self):
        return self.itemCategory


class Item(models.Model):
    itemName = models.CharField(max_length=255)
    itemCategory = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    itemMeasurement = models.DecimalField(max_digits=19, decimal_places=10)
    measurementType = models.ForeignKey(MeasurementType, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName

