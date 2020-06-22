from django.db import models

# Create your models here.
class Carousel(models.Model):
    carousel_name = models.CharField(max_length=50)
    def __str__(self):
        return self.carousel_name

class Photo(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)
    image =models.ImageField(upload_to="carousel_image", height_field=None, width_field=None, max_length=None)