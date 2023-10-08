from django.urls import path
from .views import ImageListCreateView, ImageDetailView, \
     ImageThumbnailView, ImageMediumView, ImageLargeView

urlpatterns = [
     path('images/', ImageListCreateView.as_view(), 
          name='image-list-create'),
          
     path('images/<int:pk>/', ImageDetailView.as_view(), 
          name='image-detail'),
          
     path('thumbnail/<int:pk>/', ImageThumbnailView.as_view(), 
          name='image-thumbnail'),
          
     path('medium/<int:pk>/', ImageMediumView.as_view(), 
          name='image-medium'),
          
     path('large/<int:pk>/', ImageLargeView.as_view(), 
          name='image-large'),
]
