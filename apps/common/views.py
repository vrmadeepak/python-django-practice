__author__ = "Deepak Verma"

import logging

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


logger = logging.getLogger(__name__)

__all__ = ("HealthCheck",)


class HealthCheck(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            return Response(
                {
                    "is_success": True,
                    "message": "Servers are running...",
                    "data": None,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_200_OK,
            )
