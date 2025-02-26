# Generated by Django 5.1.1 on 2024-11-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0023_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('department', models.CharField(max_length=55, null=True)),
                ('job_title', models.CharField(max_length=25, null=True)),
                ('job_description', models.TextField(max_length=300, null=True)),
                ('contact_email', models.EmailField(max_length=55, null=True)),
                ('job_code', models.CharField(max_length=20, null=True)),
                ('job_responsibilities', models.TextField(max_length=800, null=True)),
                ('job_requirement', models.TextField(max_length=800, null=True)),
                ('salary_range', models.CharField(max_length=20, null=True)),
                ('age_limit', models.CharField(max_length=20, null=True)),
                ('place', models.CharField(max_length=20, null=True)),
                ('Employement_Type', models.CharField(choices=[('Permanent', 'Permanent'), ('Contract', 'Contract'), ('none', 'none')], max_length=35, null=True)),
            ],
        ),
    ]
