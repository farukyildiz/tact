# Generated by Django 5.0.4 on 2024-05-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
