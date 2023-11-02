__author__ = "Deepak Verma"

import logging

from django.db import models
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


class Contact(models.Model):
    name = models.CharField(verbose_name="Full Name", max_length=50, db_index=True)

    phone = models.CharField(verbose_name="Phone Number", max_length=20, null=True, db_index=True)
    email = models.EmailField(verbose_name="Email", null=True, db_index=True)
    
    created_at = models.DateTimeField(_("Contact Create Date"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("Contact Update Date"), auto_now=True, db_index=True)