# Generated by Django 5.0 on 2024-01-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hm_api', '0006_posts_no_of_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
