# Generated by Django 4.2.5 on 2023-09-20 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("fisrt_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("description", models.TextField(blank=True)),
            ],
        ),
    ]