# Generated by Django 5.0 on 2024-05-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
    ]
