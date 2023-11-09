# Generated by Django 4.2.1 on 2023-05-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_name', models.CharField(max_length=200)),
                ('Bank_state', models.CharField(max_length=120)),
                ('Bank_city', models.CharField(max_length=120)),
                ('Bank_address', models.CharField(max_length=120)),
                ('BanK_code', models.IntegerField(max_length=120)),
                ('Bank_image', models.ImageField(upload_to='bank/')),
                ('Bank_feedback', models.CharField(max_length=400)),
                ('Bank_reviews', models.IntegerField(max_length=1)),
            ],
        ),
    ]