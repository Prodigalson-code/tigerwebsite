# Generated by Django 3.2.7 on 2022-05-02 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slideshow',
            old_name='slide_first_image',
            new_name='slide_image',
        ),
        migrations.RemoveField(
            model_name='slideshow',
            name='slide_second_image',
        ),
    ]