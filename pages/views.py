from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

# Create your views here.
class BlogListView(ListView):
    model = models.Post
    template_name = 'pages/home.html'

class BLogDetailView(DetailView):
    model = models.Post
    template_name = 'pages/post_detail.html'

class BlogCreateView(CreateView):
    model = models.Post
    template_name = 'pages/post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = models.Post
    template_name = 'pages/post_edit.html'
    fields = ['title', 'text']

class BlogDeleteView(DeleteView):
    model = models.Post
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('pages:posts')       # to redirect the user to posts page, it won’t execute the URL redirect until our view has finished deleting the blog post
