# Generated by Django 3.1.4 on 2020-12-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couleurs', '0003_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='user_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='round',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
