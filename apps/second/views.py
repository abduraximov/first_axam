from rest_framework import generics
from apps.second.serializers import (CompanyReviewSerializer, CompanyReviewCreateSerializer,
                                     CompanySerializer, CompanyReviewEditSerializer
                                     )
from apps.second.models import Company, Product, Review
from rest_framework import permissions
from apps.second.permissions import IsAuthorOrAdmin


class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyReviewAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyReviewSerializer


class CompanyReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = CompanyReviewCreateSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Review.objects.filter(company_id=pk)


class CompanyReviewEditAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanyReviewEditSerializer
    permission_classes = [IsAuthorOrAdmin]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Review.objects.filter(company_id=pk)


class CompanyReviewDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = CompanyReviewEditSerializer
    permission_classes = [IsAuthorOrAdmin]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Review.objects.filter(company_id=pk)
