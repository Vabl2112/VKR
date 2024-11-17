from rest_framework import serializers
from .models import Category, FAQ, Warning, Error

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = '__all__'

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = '__all__'