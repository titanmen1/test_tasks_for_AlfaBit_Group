# Generated by Django 4.1.5 on 2023-01-16 03:26

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LeadState",
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
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Название"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lead",
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
                    "name",
                    models.CharField(db_index=True, max_length=255, verbose_name="Имя"),
                ),
                (
                    "state",
                    django_fsm.FSMKeyField(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        protected=True,
                        to="task2.leadstate",
                        verbose_name="Состояние",
                    ),
                ),
            ],
        ),
    ]
