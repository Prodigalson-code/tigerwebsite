# Generated by Django 3.2.7 on 2022-05-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_servicecontent_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrysettings',
            name='facebook',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrysettings',
            name='instagram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrysettings',
            name='linkedin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrysettings',
            name='twitter',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
