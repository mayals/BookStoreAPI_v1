from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100,unique=True,null=True) 
    slug = models.SlugField(max_length=120, blank=True, null=True)
 

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

    def __str__ (self):
        return self.title 


    def get_absolute_url(self):
        return reverse('category-detail', kwargs = {'slug': self.slug})

    

    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)  # Call the "real" save() method.       
        



class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books',null=True)
    name = models.CharField(max_length=100,unique=True,null=True)
    slug = models.SlugField(max_length=120,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False,null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__ (self):
        return self.name 


    def get_absolute_url(self):
        return reverse('category-detail', kwargs = {'slug': self.slug})

    

    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)  # Call the "real" save() method.   
    

