# Generated by Django 4.2.1 on 2023-07-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_courserating'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='teacher-profile-imgs/'),
        ),
    ]