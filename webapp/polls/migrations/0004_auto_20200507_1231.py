# Generated by Django 3.0.5 on 2020-05-07 12:31

from django.db import migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200507_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='vector',
            field=polls.models.Vector(default='0'),
        ),
    ]