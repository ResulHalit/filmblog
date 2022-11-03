from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import ContentForm

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


def olustur(request):
    form = ContentForm()
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
         
    
    context={
        'form':form
    }
    return render(request, 'create.html', context)

