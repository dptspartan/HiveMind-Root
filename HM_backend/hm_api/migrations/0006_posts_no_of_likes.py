# Generated by Django 5.0 on 2024-01-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hm_api', '0005_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]