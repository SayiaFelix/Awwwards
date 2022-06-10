from django.test import TestCase
from .models import *


class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='cherry')
        self.profile = Profile.objects.create(user = self.user,bio = 'love her',contact= 43966606)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_search_profile(self):
        self.profile.save()
        profile = Profile.search_profile('cherry')
        self.assertTrue(len(profile) > 0)
    

class ProjectTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='cherry')
        self.profile = Profile.objects.create(user = self.user,bio = 'love',contact=43966606)

        self.project = Projects.objects.create(name = self.user,profile = self.profile,title = 'Awards',location='Nairobi',description='tell me',link= 'https://sirnews.herokuapp.com/',date='10/06/2022', technologies='python')

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Projects))
    

    def test_get_projects(self):
        self.project.save()
        project = Projects.get_projects()
        self.assertTrue(len(project) == 1)
    
    def test_save_project(self):
        self.project.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)
    
    def test_delete_project(self):
        self.project.delete_project()
        project = Projects.search_by_projects('Awards')
        self.assertTrue(len(project) < 1)


    def test_find_project(self):
        self.project.save()
        project = Projects.search_by_projects('Awards')
        self.assertTrue(len(project) > 0)
 
class ReviewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='cherry')

        self.review= Reviews.objects.create(user= self.user, design=10, usability=10,content=10,comment="awesome work" )

    def test_instance(self):
        self.assertTrue(isinstance(self.review, Reviews))

    def test_save_review(self):
        self.assertTrue(isinstance(self.review,Reviews))

    def test_get_reviews(self):
        self.review.save()
        review = Reviews.get_reviews()
        self.assertTrue(len(review) == 1)