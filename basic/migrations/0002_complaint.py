# Generated by Django 3.2.12 on 2022-09-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('person', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]