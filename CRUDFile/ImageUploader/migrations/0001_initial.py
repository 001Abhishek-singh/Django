# Generated by Django 4.2.1 on 2023-10-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='picture')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]