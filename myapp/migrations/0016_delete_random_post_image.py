# Generated by Django 4.1 on 2022-09-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_random'),
    ]

    operations = [
        migrations.DeleteModel(
            name='random',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='static/image'),
        ),
    ]
