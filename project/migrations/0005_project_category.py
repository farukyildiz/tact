# Generated by Django 5.0.4 on 2024-05-02 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_created_by_project_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.IntegerField(default=0),
        ),
    ]
