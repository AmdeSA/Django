# Generated by Django 3.0.5 on 2020-05-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0042_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
