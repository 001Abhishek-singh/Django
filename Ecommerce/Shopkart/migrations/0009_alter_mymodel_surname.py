# Generated by Django 4.2.1 on 2023-08-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopkart', '0008_mymodel_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='surname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
