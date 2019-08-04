from django.urls import path, include

from .views import list_images, detail_image, delete_image



urlpatterns = [
    path('', list_images),
    path('<str:slug>', detail_image),
    path('<str:slug>/delete', delete_image),
]
