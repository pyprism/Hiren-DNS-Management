# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion', '0004_auto_20161216_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotion',
            name='state',
            field=models.CharField(choices=[('Sa', 'Sad'), ('An', 'Angry'), ('Co', 'Confused'), ('Ha', 'Happy'), ('Ro', 'Romantic'), ('De', 'Depressed'), ('Si', 'Sick'), ('Ax', 'Anxious'), ('Wo', 'Worried'), ('Fr', 'Frightened')], max_length=2),
        ),
    ]
