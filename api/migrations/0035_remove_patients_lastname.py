# Generated by Django 3.2 on 2021-08-02 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20210802_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='lastname',
        ),
    ]