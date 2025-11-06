from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
#.\venv\Scripts\Activate.ps1
def home_view_blog(request):
    return render(request,'blog/blogs-page.html')
def single_blog(request):
    return render(request,'blog/single-blog.html')