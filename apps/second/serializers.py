from rest_framework import serializers
from apps.second.models import Product, Review, Company
from django.db.models import Avg
from django.contrib.auth.models import User


class CompanyProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "company",
            "discount",
        )


class CompanySerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()
    product = CompanyProductsSerializer(many=True)

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "average_rating",
            "count_review",
            "product"
        )

    def get_average_rating(self, obj):
        average_rating = Review.objects.filter(company=obj).aggregate(Avg('rating'))['rating__avg']
        return average_rating

    def get_count_review(self, obj):
        count_review = Review.objects.filter(company=obj).count()
        return count_review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name"
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = (
            "id",
            "user",
            "rating",
            "text"
        )


class CompanyReviewSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True)
    list_ratings = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "average_rating",
            "count_review",
            "list_ratings",
            "review",

        )

    def get_average_rating(self, obj):
        average_rating = Review.objects.filter(company=obj).aggregate(Avg('rating'))['rating__avg']
        return average_rating

    def get_count_review(self, obj):
        count_review = Review.objects.filter(company=obj).count()
        return count_review

    def get_list_ratings(self, obj):
        five = Review.objects.filter(company=obj, rating=5).count()
        four = Review.objects.filter(company=obj, rating=4).count()
        three = Review.objects.filter(company=obj, rating=3).count()
        two = Review.objects.filter(company=obj, rating=2).count()
        one = Review.objects.filter(company=obj, rating=1).count()
        list_ratings = [
                            {
                                "5": five,
                                "4": four,
                                "3": three,
                                "2": two,
                                "1": one
                             }
                        ]
        return list_ratings


class CompanyReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            "id",
            "user",
            "rating",
            "company",
            "text"
        )


class CompanyReviewEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            "id",
            "user",
            "rating",
            "company",
            "text"
        )
