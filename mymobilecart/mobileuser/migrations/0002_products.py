# Generated by Django 4.0.5 on 2022-06-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pro_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pro_category', models.CharField(max_length=80)),
                ('pro_name', models.CharField(max_length=80)),
                ('pro_price', models.IntegerField()),
                ('pro_specification', models.CharField(max_length=150)),
            ],
        ),
    ]
