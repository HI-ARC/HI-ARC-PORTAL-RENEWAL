# Generated by Django 2.1.2 on 2019-01-25 17:56

from django.db import migrations
import hiarc_registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('hiarc_registration', '0005_auto_20190126_0111'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='hiarcuser',
            managers=[
                ('objects', hiarc_registration.models.HiarcUserManager()),
            ],
        ),
    ]
