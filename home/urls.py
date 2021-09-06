from django.contrib import admin
from django.urls import path,include
from .views import cdetail, home,pdetail,contact

urlpatterns = [
    path('',home),
    path('postdetail/<slug:url>',pdetail),
    path('cdetail/<slug:url>',cdetail),
    path('contact/',contact),
]

handler404='home.views.errorhandler'