# Generated by Django 4.0.1 on 2022-02-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_owner_owner_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_address',
            field=models.CharField(max_length=120),
        ),
    ]
