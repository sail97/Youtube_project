
from django.urls import path
from . import views

urlpatterns = [
    path('main',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('services',views.services,name="services"),
    path('about',views.about,name="about"),
    path('dashboard',views.dashboard,name="dashboard"),
]
    