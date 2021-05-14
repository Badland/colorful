# Generated by Django 3.1.4 on 2020-12-07 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r', models.PositiveIntegerField()),
                ('g', models.PositiveIntegerField()),
                ('b', models.PositiveIntegerField()),
                ('hex', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'No answer')], default='N', max_length=1)),
                ('mail_adress', models.CharField(max_length=320)),
                ('date_joined', models.DateTimeField()),
            ],
        ),
    ]