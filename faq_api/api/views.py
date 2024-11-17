from rest_framework import generics
from .models import Category, FAQ, Warning, Error
from .serializers import CategorySerializer, FAQSerializer, WarningSerializer, ErrorSerializer

# Category Views
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# FAQ Views
class FAQListCreate(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

# Warning Views
class WarningListCreate(generics.ListCreateAPIView):
    queryset = Warning.objects.all()
    serializer_class = WarningSerializer

class WarningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warning.objects.all()
    serializer_class = WarningSerializer

# Error Views
class ErrorListCreate(generics.ListCreateAPIView):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer

class ErrorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer