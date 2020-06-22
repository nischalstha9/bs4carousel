from django.urls import path, include
from .views import CarouselView

urlpatterns = [
    path('<int:pk>/', CarouselView.as_view())
]