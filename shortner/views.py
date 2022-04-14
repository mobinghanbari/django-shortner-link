from django.shortcuts import render, HttpResponse
from .models import Url
from uuid import uuid4
# Create your views here.

def home(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
