from django.contrib import admin
from rest_framework.schemas import get_schema_view
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    path('openapi/', get_schema_view(
        title="School Service",
        description="API developers hpoing to use our service"
        ), name='openapi-schema'),
]
