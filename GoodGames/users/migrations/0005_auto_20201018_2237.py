# Generated by Django 3.1.1 on 2020-10-19 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201018_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(default=None, max_length=5, null=True),
        ),
    ]
