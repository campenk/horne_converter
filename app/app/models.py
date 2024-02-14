from django.db import models


class ItemCategory(models.Model):
    item_category = models.CharField(max_length=255)

    def __str__(self):
        return self.item_category


class Item(models.Model):

    MEASUREMENT_TYPE = [
        ("LE", "Length"),
        ("WI", "Width")
    ]

    item_name = models.CharField(max_length=255)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    item_measurement = models.DecimalField(max_digits=19, decimal_places=6)
    measurement_type = models.CharField(max_length=2, choices=MEASUREMENT_TYPE)

    def __str__(self):
        return self.item_name

