from django.urls import path

from apps.todolist import views

urlpatterns = [
    # path("v1/tasks", views.AdditionAPIView.as_view(), name="add-api"),
    # path("v1/tasks/<int:pk>/", views.AdditionAPIView.as_view(), name="add-api"),
    path("v1/tasks/add", views.AddTaskAPIView.as_view(), name="add-api"),
]
