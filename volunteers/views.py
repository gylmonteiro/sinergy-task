from django.urls import reverse_lazy
from django.views import generic
from .models import VoluntaryUser
from .forms import UserRegistrationForm
# Create your views here.

class VoluntaryUserListView(generic.ListView):
    model = VoluntaryUser
    template_name = 'list_volunteers.html'
    context_object_name = 'volunteers'


class VoluntaryUserCreateView(generic.CreateView):
    model = VoluntaryUser
    form_class = UserRegistrationForm
    template_name = 'create_voluntary.html'
    success_url = reverse_lazy("volunteers-login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


class HomeTemplateView(generic.TemplateView):
    template_name = 'home.html' 
