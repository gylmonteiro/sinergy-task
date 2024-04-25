from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('volunteers.urls')),
    path('tasks/', include('manage_tasks.urls')),
]
