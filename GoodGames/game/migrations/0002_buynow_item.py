# Generated by Django 3.1.2 on 2020-11-03 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buynow',
            name='item',
            field=models.CharField(choices=[('Ps4', 'Ps4'), ('Ps4', 'Ps4 controller'), ('Xbox', 'Xbox'), ('Xbox controller', 'Xbox controller'), ('Madden', 'Madden'), ('Nba2k21', 'Nba2k21'), ('Gaming Monitor', 'Gaming Monitor'), ('Gaming Headset', 'Gaming Headset')], default='Ps4', max_length=20),
        ),
    ]
