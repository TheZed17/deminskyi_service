# Generated by Django 3.2.16 on 2023-05-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20230524_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='comment',
            field=models.CharField(default='', max_length=50),
        ),
    ]
