# Generated by Django 5.0.2 on 2024-03-17 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0010_alter_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]