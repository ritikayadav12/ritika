# Generated by Django 4.0.1 on 2022-02-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_owner_owner_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='owner_address',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
