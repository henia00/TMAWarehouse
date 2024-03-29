# Generated by Django 5.0.2 on 2024-03-14 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('item_group', models.CharField(choices=[('0', 'GROUP0'), ('1', 'GROUP1'), ('2', 'GROUP3')], default='0', max_length=50)),
                ('unit_of_measurement', models.CharField(choices=[('0', 'UNIT0'), ('1', 'UNIT1'), ('2', 'UNIT2')], default='0', max_length=50)),
                ('quantity', models.IntegerField()),
                ('price_without_vat', models.FloatField()),
                ('status', models.CharField(max_length=300)),
                ('storage_location', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_person', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('request_id', models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('employee_name', models.CharField(max_length=100)),
                ('unit', models.CharField(choices=[('0', 'UNIT0'), ('1', 'UNIT1'), ('2', 'UNIT2')], default='0', max_length=50)),
                ('quantity', models.IntegerField()),
                ('price_without_vat', models.FloatField()),
                ('comment', models.TextField(blank=True)),
                ('status', models.CharField(default='New', max_length=20)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.items')),
            ],
        ),
    ]
