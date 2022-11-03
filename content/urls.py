from django.urls import path
from .views import *

urlpatterns = [
    path('anasayfa/', index, name="index"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path("yazi/<int:id>", yazi, name="yazi"),
    path("create/", olustur, name="create"),
]
