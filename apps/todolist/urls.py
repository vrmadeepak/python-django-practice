from django.urls import path

from apps.todolist import views

urlpatterns = [
    path("v1/tasks", views.ViewAllTasksAPIView.as_view(), name="add-api"),
    path("v1/tasks/<int:pk>/", views.TaskAPIView.as_view(), name="add-api"),
    path("v1/tasks/add", views.AddTaskAPIView.as_view(), name="add-api"),
]
