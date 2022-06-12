from django.contrib import admin
from django.urls import path,include
from awwards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('awwards.urls')),
    path('register/',views.register_user,name='register'),
    # path('ajax/register/',views.user_register,name='register'),
    path('accounts/login/',views.login_user,name='login'),
    # path('ajax/accounts/login/',views.user_login,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tinymce/', include('tinymce.urls')),
]
admin.site.site_header= "Awwwards Administration"
admin.site.site_title="Awwwards"
admin.site.index_title="Welcome to Awwards Administration"
