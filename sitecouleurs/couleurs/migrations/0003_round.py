# Generated by Django 3.1.4 on 2020-12-26 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couleurs', '0002_auto_20201207_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.date.today)),
                ('choice1', models.PositiveIntegerField()),
                ('choice2', models.PositiveIntegerField()),
                ('choice3', models.PositiveIntegerField()),
                ('ans1', models.PositiveIntegerField()),
                ('ans2', models.PositiveIntegerField()),
                ('ans3', models.PositiveIntegerField()),
                ('score', models.PositiveIntegerField()),
            ],
        ),
    ]