# Generated by Django 4.2.4 on 2023-08-29 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edusphere_app', '0004_announcement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='files',
            new_name='file',
        ),
    ]
