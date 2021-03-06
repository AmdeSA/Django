# Generated by Django 3.0.5 on 2020-04-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200415_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section1_title', models.CharField(max_length=50, unique=True)),
                ('Section1_Description', models.CharField(max_length=1000)),
                ('Section2_title', models.CharField(max_length=50, unique=True)),
                ('Section2_Description', models.CharField(max_length=1000)),
                ('Section3_title', models.CharField(max_length=50, unique=True)),
                ('Section3_Description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='home_content',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
