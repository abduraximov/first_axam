from django.urls import path
from apps.second.views import (CompanyReviewAPIView, CompanyReviewCreateAPIView,
                               CompanyDetailAPIView, CompanyReviewEditAPIView,
                               CompanyReviewDeleteAPIView)

urlpatterns = [
    path("company/<int:pk>/", CompanyDetailAPIView.as_view(), name="company-detail"),
    path("company/<int:pk>/reviews/", CompanyReviewAPIView.as_view(), name="company-reviews"),
    path("company/<int:pk>/reviews/create/", CompanyReviewCreateAPIView.as_view(), name="company-reviews-create"),
    path("reviews/<int:pk>/edit/", CompanyReviewEditAPIView.as_view(), name="company-reviews-create"),
    path("reviews/<int:pk>/delete/", CompanyReviewDeleteAPIView.as_view(), name="company-reviews-delete")
]
