from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url('profile/(\d+)', views.user_profile, name='profile'),
    url('new/profile$', views.add_user_profile, name='add_profile'),
    url('search/', views.search, name='search'),
    url('upload/', views.update_project, name='upload_project'),
    url('review/(?P<pk>\d+)',views.add_review,name='review'),
    url('all/(?P<pk>\d+)', views.all_projects, name='all'),
    url('api/profile/', views.ProfileList.as_view()),
    url('api/project/', views.ProjectList.as_view()),
    url('api-token-auth/', obtain_auth_token),
    url('api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url('api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)