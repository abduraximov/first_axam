from django.db import models
from apps.common.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    company = models.ForeignKey("first.Company",
                                on_delete=models.CASCADE,
                                related_name="vacancy",
                                null=True,
                                blank=True
                                )

    def __str__(self):
        return self.name


class Resume(BaseModel):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    vacancy = models.ForeignKey("first.Vacancy",
                                on_delete=models.CASCADE,
                                related_name="resume",
                                null=True,
                                blank=True
                                )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


