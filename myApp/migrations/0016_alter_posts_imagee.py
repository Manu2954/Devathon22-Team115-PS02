# Generated by Django 4.0.2 on 2022-09-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0015_alter_posts_imagee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='imagee',
            field=models.BinaryField(),
        ),
    ]
