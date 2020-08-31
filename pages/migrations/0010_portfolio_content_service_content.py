# Generated by Django 3.0.5 on 2020-04-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20200423_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('bio', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='service_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
