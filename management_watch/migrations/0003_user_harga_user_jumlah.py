# Generated by Django 5.0.4 on 2024-04-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_watch', '0002_remove_user_harga_remove_user_jumlah'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='harga',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='jumlah',
            field=models.IntegerField(default=0),
        ),
    ]
