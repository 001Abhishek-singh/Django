# Generated by Django 4.2.1 on 2023-08-05 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopkart', '0003_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_1', models.CharField(max_length=120, null=True)),
                ('course_2', models.CharField(max_length=120, null=True)),
                ('course_3', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_1', models.IntegerField(null=True)),
                ('staff_2', models.CharField(max_length=150, null=True)),
                ('staff_3', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subect_1', models.CharField(max_length=100, null=True)),
                ('subject_2', models.CharField(max_length=160, null=True)),
                ('subject_3', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shopkart.course')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shopkart.school')),
                ('staffs', models.ManyToManyField(to='Shopkart.staff')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shopkart.subject')),
            ],
        ),
    ]