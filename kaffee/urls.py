from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistiken/', views.statistiken, name='statistiken'),
    path('profil/', views.profil, name='profil'),
    path('einlage/', views.einlage, name='einlage'),
    path('konsum/', views.konsum, name='konsum'),
    path('kontoauszug/', views.kontoauszug, name='kontoauszug'),
    path('kontoauszug/markiere/<int:bewegung_id>/', views.markiere_bewegung, name='markiere_bewegung'),
    path('kontoauszug/markiere_modal/<int:bewegung_id>/', views.markiere_bewegung_modal, name='markiere_bewegung_modal'),
    path('kontoauszug/entmarkiere/<int:bewegung_id>/', views.entmarkiere_bewegung, name='entmarkiere_bewegung'),
]
