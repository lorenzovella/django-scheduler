# Generated by Django 3.1.1 on 2020-09-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_auto_20200929_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, max_length=200, verbose_name='Event url'),
        ),
    ]
