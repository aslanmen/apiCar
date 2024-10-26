# Generated by Django 5.1.2 on 2024-10-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('car_class', models.CharField(max_length=255)),
                ('fuel', models.CharField(max_length=255)),
                ('seat_count', models.IntegerField()),
                ('segment', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=255)),
                ('vendor', models.CharField(max_length=255)),
                ('check_in_datetime', models.DateTimeField()),
                ('check_in_office', models.CharField(max_length=255)),
                ('check_out_datetime', models.DateTimeField()),
                ('check_out_office', models.CharField(max_length=255)),
            ],
        ),
    ]
