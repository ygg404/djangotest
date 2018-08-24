from django.shortcuts import render
from dcelery.task import *
import time

# Create your views here.
#celery异步
def celeryTest(request):
    sayhello(request)
    time.sleep(3)
    return HttpResponse('celery')