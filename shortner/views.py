from django.shortcuts import render
from .models import Url
# Create your views here.

def home(request):
    return render(request, 'index.html')