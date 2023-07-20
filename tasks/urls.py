from django.urls import path
from .views import list_tasks, create_task, delete_task


# direccionamiento modulo tasks
urlpatterns = [
    path('', list_tasks),
    path('new_tasks/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task')
]