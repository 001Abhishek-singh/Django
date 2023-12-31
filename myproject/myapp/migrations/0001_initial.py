# Generated by Django 4.2.1 on 2023-05-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('course', models.CharField(max_length=150)),
                ('college', models.CharField(max_length=140)),
                ('roll', models.IntegerField(max_length=50)),
                ('condition', models.BooleanField(default=False)),
            ],
        ),
    ]
