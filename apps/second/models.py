from django.db import models
from apps.common.models import BaseModel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=64)
    company = models.ForeignKey("second.Company",
                                on_delete=models.CASCADE,
                                related_name="product",
                                null=True,
                                blank=True
                                )
    discount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="review",
                             null=True,
                             blank=True
                             )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    company = models.ForeignKey("second.Company",
                                on_delete=models.CASCADE,
                                related_name="review",
                                null=True,
                                blank=True
                                )
    text = models.TextField()

    def __str__(self):
        return self.text


