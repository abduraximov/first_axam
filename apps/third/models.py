from django.db import models
from apps.common.models import BaseModel


class CarBrand(BaseModel):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class CarModel(BaseModel):
    name = models.CharField(max_length=16)
    brand = models.ForeignKey("third.CarBrand",
                              on_delete=models.CASCADE,
                              related_name="car_model",
                              null=True,
                              blank=True)

    def __str__(self):
        return self.name


class Announcement(BaseModel):
    CURRENCY_CHOICES = (
        ('UZS', 'UZS'),
        ('EUR', 'EUR'),
        ('USD', 'USD')
    )

    model = models.ForeignKey("third.CarModel",
                              on_delete=models.CASCADE,
                              related_name="announcement",
                              null=True,
                              blank=True
                              )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=4, choices=CURRENCY_CHOICES)
    about = models.TextField()

    def __str__(self):
        return f"{self.price} {self.model.name}"

