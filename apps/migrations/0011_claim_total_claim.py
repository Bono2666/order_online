# Generated by Django 5.0 on 2024-01-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_alter_claim_additional_proposal'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='total_claim',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
    ]