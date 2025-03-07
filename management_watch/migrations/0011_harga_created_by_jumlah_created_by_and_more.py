# Generated by Django 5.0.4 on 2024-05-20 08:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_watch', '0010_alter_customuser_is_admin_alter_customuser_is_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='harga',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='harga_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jumlah',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jumlah_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='managementwatch',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='management_watch_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='merek',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='merek_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='model',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='model_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='negara',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='negara_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
