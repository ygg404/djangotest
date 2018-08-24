import time
from celery import task
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

@task
def sayhello(request):
    print('hello ...')
    time.sleep(7)
    print('world ...')
    return HttpResponse('TASK')