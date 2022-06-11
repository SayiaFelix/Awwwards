from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from .email import send_welcome_email
from django.http import JsonResponse
from django.contrib import messages
from rest_framework import status
from django.urls import reverse
from .serializer import *
from .models import *
from .forms import *

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

class ProfileList(APIView):

    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
            
class ProjectList(APIView):

    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project= self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
            review.user = current_user
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



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login(request, user)
         return redirect('homepage')
        
        else:
            messages.success(request,('Invalid information'))
            return redirect('login')
         
    else:

     return render(request,'registration/login.html')

def register_user(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             email = form.cleaned_data['email']
             send_welcome_email(username,email) 

             user = authenticate(username=username, password=password)
             login(request,user)

             messages.success(request,f'Hello {username}, Your account was Successfully Created.You will receive our email shortly.Thank You!!!')
             return redirect('add_profile')
    else:
         form = UserRegisterForm()
    return render (request,'registration/register.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))




 


