# Generated by Django 4.2 on 2023-04-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abv', models.FloatField(max_length=4)),
                ('region', models.CharField(max_length=50)),
                ('dryness', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=75)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
    ]
