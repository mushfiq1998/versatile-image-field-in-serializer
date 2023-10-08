from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer, ImageThumbnailSerializer, \
    ImageMediumSerializer, ImageLargeSerializer 

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageThumbnailView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageThumbnailSerializer

class ImageMediumView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageMediumSerializer

class ImageLargeView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageLargeSerializer
