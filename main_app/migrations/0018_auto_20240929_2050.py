# Generated by Django 3.1.1 on 2024-09-29 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_customuser_fcm_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancereport',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.student'),
        ),
    ]
