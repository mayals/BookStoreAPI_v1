# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

from django.shortcuts import render
from .models import Category,Book
from .serializers import CategorySerializer,BookSerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
        queryset  = Category.objects.all()
        serializer_class = CategorySerializer
        lookup_field = 'slug'                  # must write this to  make slug as lookup_field
 



class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class =  BookSerializer
        lookup_field = 'slug'                  # must write this to  make slug as lookup_field  