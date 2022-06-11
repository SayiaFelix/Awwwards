from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
def homepage(request):
    projects = Projects.get_projects()
    reviews = Reviews.get_reviews()
    profile = Profile.get_profile()

    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']

            review = form.save(commit=False)

            review.project = projects
            review.name = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.save()

        return redirect('homepage')

    else:
        form = ReviewForm()

    return render(request,"awwards/homepage.html",{"projects":projects, "reviews":reviews,"form": form,"profile":profile})


def user_profile(request,profile_id):

    profile = Profile.objects.get(pk = profile_id)
    projects = Projects.objects.filter(profile_id=profile).all()

    return render(request,"profile/profile.html",{"profile":profile,"projects":projects})

def add_user_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'profile/new_user_profile.html', {"form": form})