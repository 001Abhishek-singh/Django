# Generated by Django 4.2.1 on 2023-08-07 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shopkart', '0005_fromform_remove_subject_subject_2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fromform',
        ),
        migrations.DeleteModel(
            name='MyUserCreationForm',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='course',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='school',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='staffs',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
