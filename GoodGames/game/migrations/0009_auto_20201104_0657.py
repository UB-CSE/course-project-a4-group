# Generated by Django 3.1.2 on 2020-11-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20201104_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adwatch',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x10eef22e0>', max_length=1024),
        ),
        migrations.AlterField(
            model_name='buynow',
            name='name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x10eef22e0>', max_length=1024),
        ),
    ]
