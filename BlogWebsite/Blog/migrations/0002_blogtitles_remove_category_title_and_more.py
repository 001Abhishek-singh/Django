# Generated by Django 4.2.6 on 2023-10-30 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(choices=[('Wedding', 'Wedding'), ('Politics', 'Politics'), ('Climate', 'Climate'), ('Tourism', 'Toursim'), ('Employement', 'Employement'), ('History', 'History')], max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='Title',
        ),
        migrations.AddField(
            model_name='category',
            name='Category_title',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Blog.blogtitles'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Post_category_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.blogtitles'),
        ),
    ]
