# Generated by Django 3.0.5 on 2020-04-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_home_content_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_content',
            name='title',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
