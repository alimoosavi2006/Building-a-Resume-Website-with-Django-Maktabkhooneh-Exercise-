from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
#.\venv\Scripts\Activate.ps1
def home_view(request):
    return render(request,'index.html')