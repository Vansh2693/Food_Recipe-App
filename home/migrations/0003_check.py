# Generated by Django 5.0.4 on 2024-04-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_student_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Check",
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
                ("text", models.TextField()),
            ],
        ),
    ]
