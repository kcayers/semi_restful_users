from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime

from models import *
import re

def index(request):
    context = {
    "time": strftime("%B %d, %Y")
    }
    return render(request, "users/index.html", { "users": User.objects.all() }, context)

def new(request):
    return render(request, "users/new.html")


def create(request):
    #insert validation conditions
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(new)
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect(index)

def edit(request, id):
    return render(request, "users/edit.html", {"user": User.objects.get(id = id)})

def update(request, id):
    #insert validation conditions
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect(index)

def show(request, id):
    return render(request, "users/show.html", {"user": User.objects.get(id = id)})

def destroy(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect(index)
