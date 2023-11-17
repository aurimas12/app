# Generated by Django 3.2.22 on 2023-11-17 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_id', models.IntegerField(null=True)),
                ('post_url', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('salary_min', models.IntegerField(null=True)),
                ('salary_max', models.IntegerField(null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.description')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.tags')),
            ],
        ),
    ]
