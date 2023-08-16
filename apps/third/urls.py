from django.urls import path
from apps.third.views import AnnouncementAPIView


urlpatterns = [
    path("<int:pk>/", AnnouncementAPIView.as_view(), name="announcement")
]
