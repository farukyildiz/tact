# Generated by Django 5.0.4 on 2024-05-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.CharField(default='', max_length=150),
        ),
    ]
