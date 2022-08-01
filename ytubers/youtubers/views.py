from unicodedata import category
from django.shortcuts import render
from .models import Youtuber
# Create your views here.

def youtubers(request):
    youtuber=Youtuber.objects.all()
    tubers=Youtuber.objects.order_by('-created_at')
    camera_search=Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search=Youtuber.objects.values_list('category',flat=True).distinct()
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    if 'camera' in request.GET:
        camera=request.GET['camera']
        tubers = tubers.filter(camera_type__iexact=camera)
    if 'city' in request.GET:
        city=request.GET['city']
        tubers = tubers.filter(city__iexact=city)
    if 'category' in request.GET:
        category=request.GET['category']
        tubers = tubers.filter(category__iexact=category)
    data={
        'tubers': tubers,
        'camera_search' : camera_search,
        'city_search' : city_search,
        'category_search' : category_search
    }
    return render(request,'youtubers/youtubers.html',data)

def single_youtuber(request, id):
    youtuber = Youtuber.objects.get(id=id)
    data = {
        'youtuber':youtuber
    }
    return render(request,'youtubers/single_youtuber.html',data)

def search(request):
    tubers=Youtuber.objects.order_by('-created_at')
    camera_search=Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search=Youtuber.objects.values_list('category',flat=True).distinct()
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        tubers = tubers.filter(desc__contains=keyword)
    if 'camera' in request.GET:
        camera=request.GET['camera']
        tubers = tubers.filter(camera_type__iexact=camera)
    if 'city' in request.GET:
        city=request.GET['city']
        tubers = tubers.filter(city__iexact=city)
    if 'category' in request.GET:
        category=request.GET['category']
        tubers = tubers.filter(category__iexact=category)


    data = {
        'tubers' : tubers,
        'camera_search' : camera_search,
        'city_search' : city_search,
        'category_search' : category_search
    }
    print(data)
    return render(request, 'youtubers/search.html',data)