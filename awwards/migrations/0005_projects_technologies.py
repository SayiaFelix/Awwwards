# Generated by Django 3.2 on 2022-06-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0004_auto_20220610_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='technologies',
            field=models.TextField(null=True),
        ),
    ]
