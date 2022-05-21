from django.urls import path
from django.views.generic import TemplateView
from .views import TaskList, TaskDetail,AddTask

app_name = 'todo'

urlpatterns = [
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
        ), name='swagger-ui'),

    path('tasks/', TaskList.as_view(), name='tasks_list'),
    path('task-detail/<pk>/', TaskDetail.as_view(), name='tasks_detail'),
    path('add-task/', AddTask.as_view(), name="new_task"),
]
