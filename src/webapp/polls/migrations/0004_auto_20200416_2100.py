# Generated by Django 3.0.5 on 2020-04-16 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200416_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='year',
            new_name='date',
        ),
    ]
