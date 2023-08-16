from django.contrib import admin
from apps.third.models import CarBrand, CarModel, Announcement

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(Announcement)
