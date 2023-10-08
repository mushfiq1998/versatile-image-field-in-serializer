from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = VersatileImageField(upload_to='images/')
    ppoi = PPOIField('Image Point of Interest')

    # Additional fields for image variations
    thumbnail = VersatileImageField(upload_to='images/thumbnails/', 
                                    blank=True, null=True)
    medium = VersatileImageField(upload_to='images/medium/', 
                                 blank=True, null=True)
    large = VersatileImageField(upload_to='images/large/', 
                                blank=True, null=True)

     # This show image tilte to admin site
    def __str__(self):
        return self.title