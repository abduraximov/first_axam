from django.urls import path
from apps.first.views import CountAPIView

urlpatterns = [
    path("", CountAPIView.as_view(), name="count-view"),
]
