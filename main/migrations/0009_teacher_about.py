# Generated by Django 4.2.1 on 2023-07-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='about',
            field=models.TextField(default=None),
        ),
    ]
