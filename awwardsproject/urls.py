
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('awwards.urls')),
    path('tinymce/', include('tinymce.urls')),
]
admin.site.site_header= "Awwwards Administration"
admin.site.site_title="Awwwards"
admin.site.index_title="Welcome to Awwards Administration"
