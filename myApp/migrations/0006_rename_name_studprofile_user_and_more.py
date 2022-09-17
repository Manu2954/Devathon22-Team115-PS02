# Generated by Django 4.0.2 on 2022-09-17 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_clubprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studprofile',
            old_name='name',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='clubprofile',
            name='admin1',
        ),
        migrations.RemoveField(
            model_name='clubprofile',
            name='admin2',
        ),
        migrations.RemoveField(
            model_name='clubprofile',
            name='admin3',
        ),
        migrations.RemoveField(
            model_name='clubprofile',
            name='cName',
        ),
        migrations.AddField(
            model_name='clubprofile',
            name='cemaill',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='clubprofile',
            name='clubId',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='clubprofile',
            name='clubname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='clubprofile',
            name='des',
            field=models.TextField(blank=True, default=''),
        ),
    ]
