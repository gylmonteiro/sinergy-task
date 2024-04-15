from django.contrib import admin
from django.urls import path, include
from volunteers.views import HomeTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('', include('volunteers.urls')),
]
