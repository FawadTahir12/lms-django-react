# Generated by Django 4.2.1 on 2023-07-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_studentassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='student_assignment_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
