# Generated by Django 5.1.1 on 2024-11-19 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0027_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='career',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='rest.careers_us'),
        ),
    ]
