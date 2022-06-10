from django.test import TestCase
from .models import *


class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 2, username='cherry')
        self.profile = Profile.objects.create(user = self.user,bio = 'blow', phone_number= 2356789)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_search_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)


 