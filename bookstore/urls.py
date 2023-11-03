from django.urls import path

from bookstore import views

urlpatterns = [
    path("v1/books", views.BookListAPIView.as_view(), name="book-list-api"),
    path("v1/books/<int:pk>", views.BookDetailAPIView.as_view(), name="book-detail-api"),
]
