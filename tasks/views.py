from tasks.models import Taskstatus, Tag, Task
from tasks.filter import TaskFilter
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TasksViews(LoginRequiredMixin, ListView):
    model = Task


class TaskListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Task
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(self.request.GET)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    login = '/login/'
    model = Task
    template_name = 'tasks/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Task
    fields = [
        'name',
        'description',
        'status',
        'creator',
        'assigned_to',
        'tags',
    ]
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add task'
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Task
    fields = [
        'name',
        'description',
        'status',
        'creator',
        'assigned_to',
        'tags',
    ]
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit task'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskstatusListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Taskstatus
    template_name = 'statuses/task_status_list.html'


class TaskstatusCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Taskstatus
    fields = ['name']
    template_name = 'statuses/task_status_form.html'
    success_url = reverse_lazy('tasks:task_status_list')


class TaskstatusDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Taskstatus
    template_name = 'statuses/task_status_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_status_list')


class TagListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Tag
    template_name = 'tags/tag_list.html'


class TagCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Tag
    fields = ['name']
    template_name = 'tags/tag_form.html'
    success_url = reverse_lazy('tasks:tag_list')


class TagDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Tag
    template_name = 'tags/tag_confirm_delete.html'
    success_url = reverse_lazy('tasks:tag_list')
