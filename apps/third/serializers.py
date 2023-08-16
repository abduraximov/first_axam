from rest_framework import serializers
from apps.third.models import Announcement
from django.db.models import Avg, Sum


class AnnouncementSerializer(serializers.ModelSerializer):
    difference_sum = serializers.SerializerMethodField()


    class Meta:
        model = Announcement
        fields = (
            "id",
            "model",
            "price",
            "currency",
            "about",
            "difference_sum",

        )

    def get_difference_sum(self, obj):
        data = Announcement.objects.filter(model=obj.model).aggregate(Avg("price"))
        percent = obj.price / data["price__avg"] * 100
        if obj.price > data["price__avg"]:
            difference = {
                            "expensive": obj.price - data["price__avg"],
                            "percent": (obj.price - data["price__avg"]) / data["price__avg"] * 100
                          }
        if obj.price < data["price__avg"]:
            difference = {
                            "cheaper": data["price__avg"] - obj.price,
                            "percent": (data["price__avg"] - obj.price) / data["price__avg"] * 100
                        }
        data = [
            {
                "percent": percent,
                "difference": difference,
                "average_sum": data["price__avg"]
             }
        ]
        return data
