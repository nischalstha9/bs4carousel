from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Carousel, Photo
# Create your views here.
class CarouselView(DetailView):
    model = Carousel
    template_name = 'carousel.html'

# def CarouselView(request, carousel_id):
#     carousel = get_object_or_404(Carousel, pk=carousel_id)
#     return render(request, 'carousel.html',{'carousel':carousel})
