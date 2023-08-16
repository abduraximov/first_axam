from rest_framework import generics
from apps.third.serializers import AnnouncementSerializer
from apps.third.models import Announcement


class AnnouncementAPIView(generics.RetrieveAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
