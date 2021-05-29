from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
  return render(request, 'core/index.html', {
    'posts': Post.objects.all(),
  })