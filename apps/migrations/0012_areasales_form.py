# Generated by Django 5.0.1 on 2024-03-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_rename_time_arrive_order_time_arrival_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='areasales',
            name='form',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
