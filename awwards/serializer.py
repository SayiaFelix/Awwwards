from rest_framework import serializers

from awwards import forms
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_photo','bio','contact')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Projects
        fields =('id','title','name', 'description','date','technologies','location','link')



