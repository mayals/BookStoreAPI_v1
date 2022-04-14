from books.views import CategoryViewSet,BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from books import views



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('category', CategoryViewSet, basename = "category") # basename = must be class name with all small leter
router.register('book', BookViewSet, basename = "book")            # basename = must be class name with all small leter



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # # APIView
    # path('api-APIView/category/<slug:slug>', views.CategoryAPIView.as_view()),
   
    # ModelViewSet
    path('api-viewset/', include(router.urls)),
]