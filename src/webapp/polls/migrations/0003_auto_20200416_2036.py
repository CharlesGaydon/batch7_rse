# Generated by Django 3.0.5 on 2020-04-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200416_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='file_object',
            field=models.FileField(default='null', unique=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
