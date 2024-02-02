from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_form, name='contact_form'),
    path('career/', views.career, name='career'),
]