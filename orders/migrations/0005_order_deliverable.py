# Generated by Django 5.0.7 on 2024-07-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliverable',
            field=models.BooleanField(default=False),
        ),
    ]
