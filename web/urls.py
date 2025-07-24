from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('addinfo/', views.addinfo),
    path('update_item/', views.updateItem),
    path('register/', views.register),
    path('login/', views.login),
    path('camhung/', views.camhung),
    path('congnghe/', views.congnghe),
    path('kinhdi/', views.kinhdi),
    path('nauan/', views.nauan),
    path('tamly/', views.tamly),
    path('thieunhi/', views.thieunhi),
    path('tongiao/', views.tongiao),
    path('vientuong/', views.vientuong),
    path('intro/', views.intro),
    path('chinhsach/', views.chinhsach),
    path('lienhe/', views.lienhe),
    path('yeuthich/', views.yeuthich),

]