# Generated by Django 4.2.1 on 2023-05-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogModel",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("postdate", models.DateField(auto_now_add=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("business", "ビシネス"),
                            ("life", "生活"),
                            ("other", "その他"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
