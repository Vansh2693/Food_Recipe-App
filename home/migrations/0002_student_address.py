# Generated by Django 5.0.4 on 2024-04-30 22:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="address",
            field=models.TextField(blank=True),
        ),
    ]
