# Generated by Django 4.0.2 on 2022-09-16 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_studprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studprofile',
            name='course',
            field=models.CharField(choices=[('btech', 'btech'), ('mtech', 'mtech'), ('integrated_msc', 'integrated_msc')], default='btech', max_length=24),
        ),
    ]
