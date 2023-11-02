from django.urls import path

from apps.contactlist import views

urlpatterns = [
    path("v1/contacts", views.ContactsAPIView.as_view(), name="add-api"),
    path("v1/contacts/<int:pk>/", views.SingleContactAPIView.as_view(), name="add-api"),
    # path("v1/tasks/add", views.AddTaskAPIView.as_view(), name="add-api"),
]
