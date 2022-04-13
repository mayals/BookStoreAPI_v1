from rest_framework import serializers
from .models import Category,Book
# https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
# https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedrelatedfield



''' Note: you must use 'serializers.ModelSerializer' NOT USE 'serializers.HyperlinkedIdentityField' for Main classes 'CategorySerializer' AND 'BookSerializer'
    and use 'serializers.HyperlinkedIdentityField' for 'url' field and 'related_name' field inside these classes'''



        
class CategorySerializer(serializers.ModelSerializer):
    # this field to display the detail of book object 
    url = serializers.HyperlinkedIdentityField(
                                        # https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
                                        view_name = 'category-detail',   # view_name='{model_name}-detail'
                                        lookup_field = 'slug'            # change lookup_field to use slug in move between paths insteade of id 
    
    
    )
    # to desplay all books belongs to this category 
    books = serializers.HyperlinkedRelatedField(
                                        # https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
                                        view_name = 'book-detail',        # view_name='{model_name}-detail'
                                        lookup_field = 'slug',            # change lookup_field to use slug in move between paths insteade of id 
                                        many = True ,
                                        read_only = True ,
                                                                             
   )
    class Meta:
        model  = Category
        fields = ['url','id','title','slug','books']
        read_only_fields =  ['id','slug','url']                   # to  make these field only for read 
        # you can use THIS WAY, it IS ALSO TRUE instead of the field url above
        # extra_kwargs = {'url': {'lookup_field': 'slug'}}






class BookSerializer(serializers.ModelSerializer):
    
    # this foreignkey field :to show category_id  for each book object as readable (as word - not number):
    category = serializers.SlugRelatedField(
                            queryset = Category.objects.all(),
                            slug_field = 'title'  # to display category_id asredable  use title field  insead of id field 
                            ) 
   
    # this field to display the detail of book object 
    url = serializers.HyperlinkedIdentityField(
                            # https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
                            view_name = 'book-detail',   # view_name='{model_name}-detail'
                            lookup_field ='slug'         # change lookup_field to use slug in move between paths insteade of id
    )
    
    class Meta:
        model  = Book
        fields = ['url','id','category','name','slug','created_at']
        read_only_fields =  ['id','slug']                               # to  make these field only for read 
        
        # you can use THIS WAY, it IS ALSO TRUE instead of the field url above
        # extra_kwargs = {'url': {'lookup_field': 'slug'}}
