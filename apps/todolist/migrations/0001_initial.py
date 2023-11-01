# Generated by Django 4.2.6 on 2023-11-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Task Title"
                    ),
                ),
                (
                    "description",
                    models.TextField(null=True, verbose_name="Task Description"),
                ),
                (
                    "status",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="Task Status"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="Task Create Date",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="Task Update Date"
                    ),
                ),
            ],
        ),
    ]