from books.views import CategoryViewSet,BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin




# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('category-list',CategoryViewSet,basename="category-list")
router.register('book-list', BookViewSet,basename="book-list")



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-viewset/', include(router.urls)),
]