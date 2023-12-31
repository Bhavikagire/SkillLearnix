# Generated by Django 4.2.4 on 2023-08-30 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edusphere_app', '0005_rename_files_submission_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='contact_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='instructor',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=10),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='department',
            field=models.CharField(choices=[('Science', 'Science'), ('Arts', 'Arts'), ('Engineering', 'Engineering')], max_length=50),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
