from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blogs' 

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_view.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title','author','body']

class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')