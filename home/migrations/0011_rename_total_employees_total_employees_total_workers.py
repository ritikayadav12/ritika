# Generated by Django 4.0.1 on 2022-02-09 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_total_employees_alter_owner_owner_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='total_employees',
            old_name='total_employees',
            new_name='total_workers',
        ),
    ]
