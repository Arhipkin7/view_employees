# Generated by Django 3.0.2 on 2020-01-20 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200114_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Departament',
            new_name='departament',
        ),
    ]