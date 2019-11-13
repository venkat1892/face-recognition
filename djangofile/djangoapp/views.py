from django.shortcuts import render
from django.http import HttpResponse
from . models import Post


# Create your views here.
def home(request):
    
    return render(request,'code.html')
