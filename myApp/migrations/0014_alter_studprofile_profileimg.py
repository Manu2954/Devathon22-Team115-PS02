# Generated by Django 4.0.2 on 2022-09-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_rename_user_posts_cntemail_rename_image_posts_imagee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studprofile',
            name='profileImg',
            field=models.ImageField(default='img-01.png', upload_to='profile_images'),
        ),
    ]