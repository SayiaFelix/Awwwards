from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from url_or_relative_url_field.fields import URLOrRelativeURLField
import numpy as np


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_photo = models.ImageField(upload_to='profiles/',null=True)
    bio = models.CharField(max_length=240, null=True)
    contact = models.CharField(max_length=12)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)

  
    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

   
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    def delete_profile(self):
         self.delete()

    def save_profile(self):
        self.save()


class Projects(models.Model):
    name = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    project_photo = models.ImageField(upload_to = 'projects/')
    description = HTMLField(max_length=200, blank=True)
    location = models.CharField(max_length=50, blank=True)
    link = URLOrRelativeURLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    technologies =models.TextField(null=True)

    @classmethod
    def search_by_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()


    @classmethod
    def get_projects_by_profile(cls, profile):
        projects = Projects.objects.filter(profile__pk=profile)
        return projects

    @classmethod
    def get_projects(cls):
        projects = Projects.objects.all()
        return projects

    def design_rating(self):
        all_designs =list( map(lambda x: x.design, self.reviews.all()))
        return np.mean(all_designs)

    def usability_rating(self):
        all_usability =list( map(lambda x: x.usability, self.reviews.all()))
        return np.mean(all_usability)

    def content_rating(self):
        all_content =list( map(lambda x: x.content, self.reviews.all()))
        return np.mean(all_content)

    


    def __str__(self):
        return self.title


class Reviews(models.Model):
    RATING_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),)
    
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Projects,on_delete=models.CASCADE, related_name='reviews',null=True)
    design = models.IntegerField(choices=RATING_CHOICES,default=0)
    usability = models.IntegerField(choices=RATING_CHOICES,default=0)
    content = models.IntegerField(choices=RATING_CHOICES,default=0)
    comment = models.CharField(max_length=200,null=True)

    @classmethod
    def get_reviews(cls):
        reviews = Reviews.objects.all()
        return reviews
      

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField(max_length=400)
    pro_id = models.IntegerField(default=0)

