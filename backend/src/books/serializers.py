from rest_framework import serializers
from .models import Category,Book
from rest_framework.validators import UniqueValidator
# https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
# https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedrelatedfield
# https://www.django-rest-framework.org/api-guide/validators/#uniquevalidator


''' Note: you must use 'serializers.ModelSerializer' NOT USE 'serializers.HyperlinkedIdentityField' for Main classes 'CategorySerializer' AND 'BookSerializer'
    and use 'serializers.HyperlinkedIdentityField' for 'url' field and 'related_name' field inside these classes'''



        
class CategorySerializer(serializers.ModelSerializer):
    def required(value):
        if value is None:
            raise serializers.ValidationError('This field is required')

    title = serializers.CharField(required=True,validators=[required,UniqueValidator(queryset=Category.objects.all())])


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
        fields = ['id','url','title','slug','books']
        read_only_fields =  ['id','url','slug','books']                   # to  make these field only for read 
        # you can use THIS WAY, it IS ALSO TRUE instead of the field url above
        # extra_kwargs = {'url': {'lookup_field': 'slug'}}
        
        extra_kwargs = {'title': {'required': True}} # to not enter title=None value ,that makes error in database 







class BookSerializer(serializers.ModelSerializer):

    def required(value):
        if value is None:
            raise serializers.ValidationError('This field is required')
    
    name = serializers.CharField(required=True,validators=[required,UniqueValidator(queryset=Book.objects.all())])

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
        fields = ['id','url','slug','category','name','created_at']
        read_only_fields =  ['id','url','slug','category']                               # to  make these field only for read 
        
        # you can use THIS WAY, it IS ALSO TRUE instead of the field url above
        # extra_kwargs = {'url': {'lookup_field': 'slug'}}
        
        extra_kwargs = {'name': {'required': True}}   # to not enter name=None value ,that makes error in database 