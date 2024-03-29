# Generated by Django 5.0 on 2023-12-27 03:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "hm_api",
            "0002_friends_created_at_friends_from_user_friends_to_user_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Posts",
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
                ("caption", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_who_posted",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
