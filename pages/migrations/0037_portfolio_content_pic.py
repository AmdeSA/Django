# Generated by Django 3.0.5 on 2020-05-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_auto_20200513_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_content',
            name='pic',
            field=models.ImageField(null=True, upload_to='static/img/portfolio'),
        ),
    ]
