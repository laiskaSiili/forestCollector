from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Person, Video, StandInformation
from .forms import PersonForm, VideoForm, StandInformationForm

import random

@login_required
def forest_collector(request):
    context = {}
    if request.method == "POST":
        form = StandInformationForm(request.POST)
        if form.is_valid():
            StandInformation.objects.create(**form.cleaned_data)
            return redirect(reverse('forrestcollector'))
        else:
            context["form"] = form
    elif request.method == "GET":
        form = StandInformationForm()
        context["form"] = form
    return render(request, 'forestcollector/include/forestcollectorform.html', context)


########################
########################

# Redirect all bad requests that don't match an url pattern to home (only with DEBUG = False)
def bad_request(request, *args, **kwargs):
    return redirect('home')

def home(request):
    all_people = Person.objects.all().order_by('age')
    context = {
        'people': all_people
        }
    return render(request, 'forestcollector/include/namedisplay.html', context)

def register(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(**form.cleaned_data)
            return redirect(reverse('home'))
    elif request.method == "GET":
        form = PersonForm()
    return render(request, 'forestcollector/include/register.html', {'form': form})

def printSection(request, chapter, section):
    ctx = {
        'chapter': chapter,
        'section': section
    }
    return render(request, 'forestcollector/include/section.html', ctx)


def showvideo(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = VideoForm()
        else:
            print(form)
    elif request.method == "GET":
        form = VideoForm()
    lastvideo= Video.objects.last()
    
    context= {
        'lastvideo': lastvideo,
        'form': form
    }

    return render(request, 'forestcollector/include/video.html', context)