# Generated by Django 2.1.7 on 2019-03-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190320_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(default='static/default.png', upload_to='static/'),
        ),
    ]
