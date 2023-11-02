__author__ = "Deepak Verma"

import logging

import decimal

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contactlist.models import Contact

logger = logging.getLogger(__name__)

__all__ = ("ContactsAPIView", "SingleContactAPIView")


class ContactsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        logger.info(f"[VIEW ALL CONTACTS] > query_params > {request.query_params}")
        try:
            contacts = Contact.objects.all().order_by('name', 'created_at')
            data = [{
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email,
                "date_created": contact.created_at,
                "date_updated": contact.updated_at
            } for contact in contacts]
            
            return Response(
                {
                    "is_success": True,
                    "message": None,
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.error(f"[VIEW ALL CONTACTS] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    def post(self, request, format=None):
        logger.info(f"[ADD NEW CONTACT] > Payload > {request.payload}")
        try:
            name = request.data.get("name", "").strip().title()
            phone = request.data.get("phone", "").strip()
            email = request.data.get("email", "").strip()

            if not name:
                raise ValueError("Name cannot be empty.")
            if not (email or phone):
                raise ValueError("Email or phone number is required to save.")
            
            contact = Contact.objects.create(
                name=name,
                phone=phone,
                email=email
            )

            data = {
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email,
                "date_created": contact.created_at,
                "date_updated": contact.updated_at
            }
            
            return Response(
                {
                    "is_success": True,
                    "message": "Created",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.error(f"[ADD NEW CONTACT] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )


class SingleContactAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        logger.info(f"[GET CONTACT] > PK > {pk}")
        try:
            contact = Contact.objects.get(id=pk)
            data = {
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email,
                "date_created": contact.created_at,
                "date_updated": contact.updated_at
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
            logger.error(f"[GET CONTACT] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
    def put(self, request, pk, format=None):
        logger.info(f"[UPDATE CONTACT] > Payload > {request.data} > PK > {pk}")
        try:
            name = request.data.get("name", "").strip().title()
            phone = request.data.get("phone", "").strip()
            email = request.data.get("email", "").strip()

            contact = Contact.objects.get(id=pk)

            contact_updated = False
            if name and name != contact.name:
                contact.name = name
                contact_updated = True
            if phone and phone != contact.phone:
                contact.phone = phone
                contact_updated = True
            if email and email != contact.email:
                contact.email = email
                contact_updated = True
            contact.save()

            data = {
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email,
                "date_created": contact.created_at,
                "date_updated": contact.updated_at
            }
            
            return Response(
                {
                    "is_success": True,
                    "message": "Updated" if contact_updated else "Nothing to update",
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.error(f"[UPDATE CONTACT] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk, format=None):
        logger.info(f"[DELETE CONTACT] > PK {pk}")
        try:
            contact = Contact.objects.filter(id=pk).first()
            if not contact:
                raise ValueError(f"Contact with id: {pk} does not exist")
            contact.delete()
            
            return Response(
                {
                    "is_success": True,
                    "message": "Deleted Successfully",
                    "data": None,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            logger.error(f"[DELETE CONTACT] > Exception > {ex.__str__()}")
            return Response(
                {"is_success": False, "message": ex.__str__(), "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )

