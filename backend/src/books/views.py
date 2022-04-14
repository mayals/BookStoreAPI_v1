# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
# https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py 


from django.shortcuts import render
from .models import Category,Book
from .serializers import CategorySerializer,BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404




class CategoryViewSet(viewsets.ViewSet):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'                 # must write this to  make slug as lookup_field

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True,context = {'request': request})
        return Response(serializer.data)


    def retrieve(self, request, slug=None):
        queryset = self.queryset
        category = get_object_or_404(queryset, slug=slug)
        serializer = self.serializer_class(category, many = False, context = {'request': request})
        return Response(serializer.data)


    def create(self, request):
        serializer = self.serializer_class(data= request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                            

    
    def update(self, request, slug=None, *args, **kwargs):
        queryset = self.queryset
        category = get_object_or_404(queryset, slug=slug)
        serializer = self.serializer_class(category, data = request.data, context = {'request': request}, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save(slug=slug, **serializer.validated_data)
        return Response(serializer.validated_data)
       
       
    def destroy(self, request, slug=None, *args, **kwargs):
        queryset = self.queryset
        category = get_object_or_404(queryset, slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

    
           
           
        







class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()
    serializer_class =  BookSerializer
    lookup_field = 'slug'                  # must write this to  make slug as lookup_field  
    
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True,context = {'request': request})
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        serializer = BookSerializer(book, many = False, context = {'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data= request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)   
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, slug=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        serializer = CategorySerializer(category, data= request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)   
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


        
    def destroy(self, request, slug=None, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











# class CategoryAPIView(APIView):
#     def get_object(self, slug):
#         try:
#             return Category.objects.get(slug=slug)
#         except Category.DoesNotExist:
#             raise Http404

#     def put(self, request, slug, format=None):
#             category = self.get_object(slug)
#             serializer = CategorySerializer(category, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

