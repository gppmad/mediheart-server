# Generated by Django 3.2 on 2021-08-02 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_remove_patients_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='birthDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patients',
            name='bloodType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bloodtype'),
        ),
    ]
