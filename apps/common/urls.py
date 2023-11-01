from django.urls import path

from apps.common import views

urlpatterns = [
    path("", views.HealthCheck.as_view(), name="health"),
    path("health", views.HealthCheck.as_view(), name="health-api"),
]
