# Generated by Django 5.0.4 on 2024-05-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summery', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('project', models.IntegerField()),
                ('category', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
