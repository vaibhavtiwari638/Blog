# Generated by Django 4.1 on 2022-09-29 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_delete_random_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
