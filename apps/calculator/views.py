__author__ = "Deepak Verma"

import logging

import decimal

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


logger = logging.getLogger(__name__)

__all__ = ("HealthCheck",)


class AdditionAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            num1 = request.data["num1"]
            num2 = request.data["num2"]
            result = num1 + num2
            data = {
                "num1": num1,
                "num2": num2,
                "result": result
            }
            return Response(
                {
                    "is_success": True,
                    "message": "",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_200_OK,
            )

class SubtractionAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            num1 = request.data["num1"]
            num2 = request.data["num2"]
            result = num1 - num2
            data = {
                "num1": num1,
                "num2": num2,
                "result": result
            }
            return Response(
                {
                    "is_success": True,
                    "message": "",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_200_OK,
            )

class DivisionAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            num1 = request.data["num1"]
            num2 = request.data["num2"]
            result = num1 / num2
            data = {
                "num1": num1,
                "num2": num2,
                "result": result
            }
            return Response(
                {
                    "is_success": True,
                    "message": "",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_200_OK,
            )

class MultiplicationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            num1 = request.data["num1"]
            num2 = request.data["num2"]
            result = num1 * num2
            data = {
                "num1": num1,
                "num2": num2,
                "result": result
            }
            return Response(
                {
                    "is_success": True,
                    "message": "",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_200_OK,
            )
