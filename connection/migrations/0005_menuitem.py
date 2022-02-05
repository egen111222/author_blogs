# Generated by Django 3.2.7 on 2021-10-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0004_social_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]
