from rest_framework import serializers
from .models import Category,Book



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id','title','slug','books']
        lookup_field='slug'



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = ['id','category','name','slug','created_at']
        lookup_field='slug'