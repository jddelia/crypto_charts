from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainsite-index'),
    path('btc/', views.btc, name='mainsite-btc'),
    path('eth/', views.eth, name='mainsite-eth'),
    path('ltc/', views.ltc, name='mainsite-ltc'),
    path('contact/', views.contact, name='mainsite-contact')
]
