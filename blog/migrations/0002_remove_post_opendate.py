# Generated by Django 2.2.3 on 2019-08-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='opendate',
        ),
    ]