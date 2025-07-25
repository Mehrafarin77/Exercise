from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepageview(request):
    print(f'Request: {request}')
    return HttpResponse('Hello, world!')