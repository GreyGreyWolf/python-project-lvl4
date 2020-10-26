from django.urls import path
from tasks import views


app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list',),
    path('new/',
         views.TaskCreateView.as_view(), name='task_add',),
    path('<int:pk>',
         views.TaskDetailView.as_view(), name='task_detail',),
    path('<int:pk>/edit',
         views.TaskUpdateView.as_view(), name='task_edit',),
    path('<int:pk>/delete',
         views.TaskDeleteView.as_view(), name='task_delete',),
    path('statuses/',
         views.TaskstatusListView.as_view(), name='task_status_list', ),
    path('statuses/new',
         views.TaskstatusCreateView.as_view(), name='task_status_add',),
    path('statuses/<int:pk>/delete',
         views.TaskstatusDeleteView.as_view(), name='task_status_delete',),
    path('tags/',
         views.TagListView.as_view(), name='tag_list',),
    path('tags/new',
         views.TagCreateView.as_view(), name='tag_add',),
    path('tags/<int:pk>/delete',
         views.TagDeleteView.as_view(), name='tag_delete',),
]
