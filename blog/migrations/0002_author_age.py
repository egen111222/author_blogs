# Generated by Django 3.2.7 on 2021-12-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]