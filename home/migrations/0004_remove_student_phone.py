# Generated by Django 5.0.4 on 2024-04-30 22:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_check"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="phone",
        ),
    ]
