from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models

# Create your views here.
class BlogListView(ListView):
    model = models.Post
    template_name = 'pages/home.html'

class BLogDetailView(DetailView):
    model = models.Post
    template_name = 'pages/post_detail.html'