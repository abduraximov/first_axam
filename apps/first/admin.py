from django.contrib import admin
from apps.first.models import Vacancy, Company, Resume

admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Resume)
