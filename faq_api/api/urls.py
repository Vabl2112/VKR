from django.urls import path
from .views import (
    CategoryListCreate, CategoryDetail,
    FAQListCreate, FAQDetail,
    WarningListCreate, WarningDetail,
    ErrorListCreate, ErrorDetail
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    # FAQ URLs
    path('faqs/', FAQListCreate.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', FAQDetail.as_view(), name='faq-detail'),

    # Warning URLs
    path('warnings/', WarningListCreate.as_view(), name='warning-list-create'),
    path('warnings/<int:pk>/', WarningDetail.as_view(), name='warning-detail'),

    # Error URLs
    path('errors/', ErrorListCreate.as_view(), name='error-list-create'),
    path('errors/<int:pk>/', ErrorDetail.as_view(), name='error-detail'),
]