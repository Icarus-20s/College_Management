# Generated by Django 3.1.1 on 2024-09-29 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20240929_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fcm_token',
        ),
    ]
