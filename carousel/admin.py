from django.contrib import admin
from .models import Carousel, Photo
# Register your models here.
class PhotoInline(admin.TabularInline):
    model= Photo
    extra= 3

class CarouselAdmin(admin.ModelAdmin):
    inlines=[PhotoInline]
admin.site.register(Carousel, CarouselAdmin)