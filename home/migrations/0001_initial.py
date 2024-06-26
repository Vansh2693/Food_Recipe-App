# Generated by Django 5.0.4 on 2024-04-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("phone", models.PositiveBigIntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("image", models.ImageField(upload_to="")),
                ("file", models.FileField(upload_to="")),
            ],
        ),
    ]
