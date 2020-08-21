# Generated by Django 3.0.8 on 2020-08-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=100)),
                ('buying_currency', models.FloatField()),
                ('selling_currency', models.FloatField()),
                ('difference', models.FloatField()),
                ('currency_code', models.CharField(max_length=100)),
            ],
        ),
    ]