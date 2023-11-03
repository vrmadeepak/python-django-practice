__author__ = "Deepak Verma"

import logging

import decimal

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from bookstore.models import Author, Book

logger = logging.getLogger(__name__)

# __all__ = ("HealthCheck",)


class BookListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        logger.info(f"[VIEW BOOKS] > Payload > {request.query_params}")
        try:
            # data = request.data
            # title = data.get("title", "").strip().title()
            # author = data.get("author", "").strip().title()
            # price = data.get("price", None)
            # quantity = data.get("quantity", None)
            # publication_date = data.get("publication_date", None)
            # categories = data.get("categories", None)

            # author = Author.objects.filter(name__iexact=author).first()

            books = Book.objects.all()
            
            data = [{
                "id": book.id,
                "title": book.title,
                "author": book.author.name if book.author_id else None,
                "price": book.price,
                "quantity": book.quantity,
                "publication_date": book.publication_date,
                "categories": [category.name for category in book.categories.all()],
                "date_created": book.created_at,
                "date_updated": book.updated_at
            }for book in books]

            return Response(
                {
                    "is_success": True,
                    "message": "Created Successfully",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.info(f"[ADD A NEW BOOK] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    def post(self, request, format=None):
        logger.info(f"[ADD A NEW BOOK] > Payload > {request.data}")
        try:
            data = request.data
            title = data.get("title", "").strip().title()
            author = data.get("author", "").strip().title()
            price = data.get("price", None)
            quantity = data.get("quantity", None)
            publication_date = data.get("publication_date", None)
            categories = data.get("categories", None)

            author = Author.objects.filter(name__iexact=author).first()

            Book.objects.create(
                title=title,
                author=author,
                price=price,
                quantity=quantity,
                publication_date=publication_date
            )
            
            return Response(
                {
                    "is_success": True,
                    "message": "Created Successfully",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.info(f"[ADD A NEW BOOK] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )


class BookDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        logger.info(f"[VIEW BOOK USING ID] > Payload > {request.query_params}")
        try:
            # data = request.data
            # title = data.get("title", "").strip().title()
            # author = data.get("author", "").strip().title()
            # price = data.get("price", None)
            # quantity = data.get("quantity", None)
            # publication_date = data.get("publication_date", None)
            # categories = data.get("categories", None)

            # author = Author.objects.filter(name__iexact=author).first()

            book = Book.objects.filter(pk=pk).first()
            # print(book.pk)

            if not book:
                raise ValueError(f"Book with id: {pk} does not exist!")
            else:
                data = {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author.name if book.author_id else None,
                    "price": book.price,
                    "quantity": book.quantity,
                    "publication_date": book.publication_date,
                    "categories": [category.name for category in book.categories.all()],
                    "date_created": book.created_at,
                    "date_updated": book.updated_at
                }
            
            return Response(
                {
                    "is_success": True,
                    "message": "Created Successfully",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.info(f"[VIEW BOOK USING ID] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    def put(self, request, pk, format=None):
        logger.info(f"[ADD A NEW BOOK] > Payload > {request.data}")
        try:
            data = request.data
            title = data.get("title", "").strip().title()
            author = data.get("author", "").strip().title()
            price = data.get("price", None)
            quantity = data.get("quantity", None)
            publication_date = data.get("publication_date", None)
            categories = data.get("categories", None)

            author = Author.objects.filter(name__iexact=author).first()

            Book.objects.create(
                title=title,
                author=author,
                price=price,
                quantity=quantity,
                publication_date=publication_date
            )
            
            return Response(
                {
                    "is_success": True,
                    "message": "Created Successfully",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.info(f"[ADD A NEW BOOK] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )
