# Generated by Django 5.1.2 on 2024-11-15 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseContactNumber',
            fields=[
                ('uid', models.OneToOneField(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.user')),
                ('contactnumber', models.CharField(db_column='ContactNumber', max_length=255)),
            ],
            options={
                'db_table': 'use_contact_number',
                'managed': False,
            },
        ),
    ]
