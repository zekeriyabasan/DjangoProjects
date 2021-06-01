from django.shortcuts import render
from django.views.generic import TemplateView # Drf olmaması için gömülü template
# Create your views here.


class AnaSayfaView(TemplateView): # sınıf tabanlı generic vievler kullanılıyor artık
    template_name = 'home.html'
     # bundan sonra url leri güncellemek gerekir 2 yerde güncelliyoruz projed urls te ve app urls te
     # app te urls dosyası aç from django.urls import path ve from .vievs import AnasayfaViews

class HakkindaView(TemplateView):
    template_name = 'hakkinda.html'