# Generated by Django 3.1.1 on 2020-12-07 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament', '0009_auto_20201206_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament_winner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='no_of_players',
            field=models.IntegerField(choices=[(4, 4), (8, 8), (16, 16), (32, 32)]),
        ),
    ]
