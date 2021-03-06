# Generated by Django 2.2.4 on 2020-06-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kosdaq_by_10second',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='Kospi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=True)),
                ('fluctuation', models.FloatField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kospi_by_10second',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
