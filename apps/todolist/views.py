__author__ = "Deepak Verma"

import logging

import decimal

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.todolist.models import Task

logger = logging.getLogger(__name__)

__all__ = ("HealthCheck",)


class AddTaskAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            title = request.data.get("title", "").strip().title()
            if not title:
                raise ValueError("Title missing")
            
            description = request.data.get("description", "").strip()
            
            task = Task.objects.create(
                title=title,
                description=description if description else None,
            )
            
            return Response(
                {
                    "is_success": True,
                    "message": "Task Successfully Created",
                    "data": {
                        "title": title,
                        "status": "Incomplete" if not task.status else "Completed"
                    },
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_200_OK,
            )
