from rest_framework import serializers
from .models import Category,Book





class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="book-api-detail",)                     # book detail link 
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='title') # this foreignkey field :to show cat_id readable (as word - not number)
    
    class Meta:
        model  = Book
        fields = ['url','id','category','name','slug','created_at']
        # lookup_field='slug'



        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="category-api-detail",)          # category detail link 
    books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-api-detail') 
    
    class Meta:
        model  = Category
        fields = ['url','id','title','slug','books']
        # lookup_field='slug'
        # extra_kwargs = {
        #     'url': {'view_name': 'category-detail'}
        # }