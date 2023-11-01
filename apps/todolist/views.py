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


class ViewAllTasksAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            tasks = Task.objects.all().order_by('created_at')
            data = [{
                "title": task.title,
                "description": task.description,
                "status": "Incomplete" if not task.status else "Completed",
                "date_created": task.created_at,
                "date_updated": task.updated_at
            } for task in tasks]
            
            return Response(
                {
                    "is_success": True,
                    "message": None,
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_200_OK,
            )


class TaskAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            task = Task.objects.get(id=pk)
            data = {
                "title": task.title,
                "description": task.description,
                "status": "Incomplete" if not task.status else "Completed",
                "date_created": task.created_at,
                "date_updated": task.updated_at
            }
            
            return Response(
                {
                    "is_success": True,
                    "message": None,
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_200_OK,
            )
        
    def put(self, request, pk, format=None):
        try:
            title = request.data.get("title", "").strip().title()
            description = request.data.get("description", "").strip()
            task_status = request.data.get("status", None)

            task = Task.objects.get(id=pk)

            task_updated = False
            if title and title != task.title:
                task.title = title
                task_updated = True
            if description and description != task.description:
                task.description = description
                task_updated = True
            if task_status and task_status != task.status:
                task.status = task_status
                task_updated = True
            task.save()

            data = {
                "title": task.title,
                "description": task.description,
                "status": "Incomplete" if not task.status else "Completed",
                "date_created": task.created_at,
                "date_updated": task.updated_at
            }
            
            return Response(
                {
                    "is_success": True,
                    "message": "Updated" if task_updated else "Nothing to update",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_200_OK,
            )

    def delete(self, request, pk, format=None):
        try:
            # title = request.data.get("title", "").strip().title()
            # description = request.data.get("description", "").strip()
            # task_status = request.data.get("status", None)

            task = Task.objects.filter(id=pk).first()
            if not task:
                raise ValueError(f"Task with id: {pk} does not exist")
            task.delete()
            
            return Response(
                {
                    "is_success": True,
                    "message": "Deleted Successfully",
                    "data": None,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_200_OK,
            )


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
