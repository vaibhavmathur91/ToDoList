from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from myapp.models import DoTaskList

class TaskList(ListView):
    template_name = 'myapp/index.html'
    
    def get_queryset(self):
        return DoTaskList.objects.all()

class TaskCreate(CreateView):
    template_name = 'myapp/task_form.html'
    model = DoTaskList
    fields = ['name']
    success_url = reverse_lazy('index')

class TaskUpdate(UpdateView):
    template_name = 'myapp/task_form.html'
    model = DoTaskList
    fields = ['name', 'completed']
    success_url = reverse_lazy('index')

class TaskDelete(DeleteView):
    template_name = 'myapp/task_form.html'
    model = DoTaskList
    success_url = reverse_lazy('index')