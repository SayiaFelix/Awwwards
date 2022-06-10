# Generated by Django 3.2 on 2022-06-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
    ]
