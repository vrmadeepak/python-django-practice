__author__ = "Deepak Verma"

import logging

from django.db import models
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


class Task(models.Model):
    title = models.CharField(verbose_name="Task Title", max_length=200, db_index=True)

    description = models.TextField(verbose_name="Task Description", null=True)
    status = models.BooleanField(verbose_name="Task Status", default=False, db_index=True)
    
    created_at = models.DateTimeField(_("Task Create Date"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("Task Update Date"), auto_now=True, db_index=True)