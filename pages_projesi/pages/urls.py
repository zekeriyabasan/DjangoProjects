from django.urls import path
from .views import AnaSayfaView
from .views import HakkindaView
urlpatterns = [
     path('',AnaSayfaView.as_view(),name = 'anasayfa'),
     path('hakkinda/',HakkindaView.as_view(),name = 'hakkinda') # sınıf tabanlı view kullandığımız için sonuna as_view() ekledik
]