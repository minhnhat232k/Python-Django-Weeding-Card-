# Generated by Django 3.2.3 on 2021-05-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('time', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'subscribe8',
            },
        ),
    ]
