# Generated by Django 3.1.4 on 2021-01-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210101_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='letters',
            field=models.CharField(default=None, max_length=27),
        ),
    ]
