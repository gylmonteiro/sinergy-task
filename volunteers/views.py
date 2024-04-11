from django.shortcuts import render
from django.views import generic
from .models import VoluntaryUser
from .forms import VoluntaryUserForm
# Create your views here.

class VoluntaryUserListView(generic.ListView):
    model = VoluntaryUser
    template_name = 'list_volunteers.html'
    context_object_name = 'volunteers'


class VoluntaryUserCreateView(generic.CreateView):
    model = VoluntaryUser
    form_class = VoluntaryUserForm
    template_name = 'create_voluntary.html'


class HomeTemplateView(generic.TemplateView):
    template_name = 'home.html' 
