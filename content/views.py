from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    content = Content.objects.all()
    context = {
        "content": content
    }
    return render(request, "index.html", context)

def contact(request):
    
    return render(request, "contact.html")

def about(request):
    
    return render(request, "about.html")


def yazi(request, id):
    post = Content.objects.filter(id=id)
    context = {
        "post":post
    }
    
    return render(request, "content.html", context)