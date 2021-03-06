# Generated by Django 3.1.1 on 2020-12-06 23:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_tournament_started'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournamentmatch',
            old_name='game_no',
            new_name='bracketNo',
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='bye',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='lastGames',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='nextGame',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='roundNo',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='teamnames',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=[], size=None),
            preserve_default=False,
        ),
    ]
