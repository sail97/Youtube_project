from django.urls import path
from . import views

urlpatterns = [
   path('featured',views.youtubers,name='youtubers'),
   path('youtuber/<int:id>',views.single_youtuber,name='single_youtuber'),
   path('search',views.search,name='search')
]