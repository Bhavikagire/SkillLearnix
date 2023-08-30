# Generated by Django 4.2.4 on 2023-08-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edusphere_app', '0002_course_rename_departmentid_department_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('files', models.FileField(upload_to='submissions/')),
                ('comments', models.TextField(blank=True, null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edusphere_app.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edusphere_app.student')),
            ],
        ),
    ]