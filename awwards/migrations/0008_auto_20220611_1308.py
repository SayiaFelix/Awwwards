# Generated by Django 3.2 on 2022-06-11 10:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0007_projects_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=tinymce.models.HTMLField(blank=True, max_length=300),
        ),
    ]
