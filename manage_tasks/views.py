from django.views import generic
from .models import Task
from .forms import TaskModelForm
# Create  your views here.


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskModelForm
    success_url = '/'
    template_name = 'create_task.html'

    def form_valid(self, form):
        voluntary = self.request.user
        form.instance.voluntary = voluntary
        form.save()
        return super().form_valid(form)


class TaskListView(generic.ListView):
    model = Task
    template_name = 'list_tasks.html'
    context_object_name = 'tasks'

    # def get_queryset(self):
    #     tasks = super().get_queryset()
    #     tasks_voluntary = tasks.filter(voluntary=self.request.user)
    #     return tasks_voluntary
