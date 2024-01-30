from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    import datetime
    mes = 'Time now from python backend\n'+str(datetime.datetime.now())
    data = {"message": mes}
    return JsonResponse(data)

# Create your views here.
