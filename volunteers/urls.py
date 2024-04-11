from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("login", LoginView.as_view(template_name="login.html"), name="volunteers-login"),
    path("logout/", LogoutView.as_view(), name="volunteers-logout"),
    path("list/", views.VoluntaryUserListView.as_view(), name="volunteers-list"),
    path("create/", views.VoluntaryUserCreateView.as_view(), name="volunteers-create"),
]
