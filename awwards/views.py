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

def search(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_project = Projects.search_by_projects(search_term)
        message = search_term

        return render(request,'awwards/search.html',{"message":message,
                                             "searched_project":searched_project})
    else:
        message = "You haven't searched for any project"
        return render(request,'awwards/search.html',{"message":message})

def update_project(request):
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.posted_by = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('homepage')
            else:
                form = UploadForm()
            return render(request,'awwards/upload_project.html',{"user":current_user,"form":form})

def add_review(request,pk):
    project = get_object_or_404(Projects, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = form.save(commit=False)
            review.project = project
            review.juror = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.save()
            return redirect('homepage')
    else:
        form = ReviewForm()
        return render(request,'awwards/review.html',{"user":current_user,"form":form})


def all_projects(request, pk):
    profile = Profile.objects.get(pk=pk)
    projects = Projects.objects.all().filter(name_id=pk)

    return render(request, 'profile/profile.html', {"profile": profile,'projects': projects,} )