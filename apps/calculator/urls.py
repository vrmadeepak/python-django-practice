from django.urls import path

from apps.calculator import views

urlpatterns = [
    path("v1/add", views.AdditionAPIView.as_view(), name="add-api"),
    path("v1/subtract", views.SubtractionAPIView.as_view(), name="subtract-api"),
    path("v1/multiply", views.MultiplicationAPIView.as_view(), name="multiply-api"),
    path("v1/divide", views.DivisionAPIView.as_view(), name="divide-api"),
]
