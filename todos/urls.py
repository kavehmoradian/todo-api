from django.urls import path
from .views import TaskList, TaskDetail,AddTask

app_name = 'todo'

urlpatterns = [
    #path('', api_docs, name='api_docs'),
    path('tasks/', TaskList.as_view(), name='tasks_list'),
    path('task-detail/<pk>/', TaskDetail.as_view(), name='tasks_detail'),
    path('add-task/', AddTask.as_view(), name="new_task"),
]
