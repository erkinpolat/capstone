# Generated by Django 3.0.10 on 2020-10-01 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='bosy',
            new_name='body',
        ),
    ]
