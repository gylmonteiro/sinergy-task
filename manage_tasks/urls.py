from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='create-task' ),
    path('', views.TaskListView.as_view(), name='list-tasks')
]
