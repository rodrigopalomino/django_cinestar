from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("peliculas/<str:id>", views.peliculas),
    path("pelicula/<int:id>", views.pelicula, name="pelicula"),
    path("cines", views.cines),
    path("cine/<int:id>", views.cine, name="cine"),
]
