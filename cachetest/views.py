from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import  cache

# Create your views here.
# @cache_page(60)
def cache1(request):
    # cache.set("key1","no" ,500)
    print (cache.get("key1"))
    return render(request, "cache1.html");

