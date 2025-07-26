from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def homepageview(request):
#     print(f'Request: {request}')
#     return HttpResponse('Hello, world!')


class HomePageView(TemplateView):           # new
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):          # new
    template_name = 'pages/about.html'