# Generated by Django 5.0.2 on 2024-03-17 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_rename_item_id_orders_item_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='item_name',
            new_name='item_id',
        ),
    ]
