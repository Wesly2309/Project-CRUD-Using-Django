# Generated by Django 5.0.4 on 2024-05-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_watch', '0009_alter_customuser_is_admin_alter_customuser_is_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='admin status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='user status'),
        ),
    ]
