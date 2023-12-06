from django.urls import path

from task_tracker.views import TaskListView, TaskDetailView, TaskStatusView


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks-list'),
    path('<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('status', TaskStatusView.as_view(), name='tasks-status'),
]
