# Generated by Django 3.0.2 on 2020-01-14 13:01

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('second_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('date_of_birth', models.DateTimeField()),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('start_date', models.DateTimeField()),
                ('stop_date', models.DateTimeField(blank=True, null=True)),
                ('role', models.CharField(choices=[('admin', 'Administrator'), ('backend', 'back-end dev'), ('frontend', 'Front-end dev')], default='admin', max_length=32)),
                ('Departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Department')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
    ]
