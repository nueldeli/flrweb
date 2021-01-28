from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddPostForm, UpdatePostForm
from django.urls import reverse_lazy

# Create your views here.
class PostView(ListView):
	model = Post
	template_name = 'blog/post_index.html'
	ordering = ['-date_written']

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'blog/post_add.html'
	form_class = AddPostForm

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'blog/post_update.html'
	form_class = UpdatePostForm

class DeletePostView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('post_index')
