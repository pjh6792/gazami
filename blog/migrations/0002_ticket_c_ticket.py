# Generated by Django 2.2.1 on 2019-08-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='c_ticket',
            field=models.CharField(choices=[('T1', 'Ticket1'), ('T2', 'Ticket2'), ('T3', 'Ticket3'), ('T4', 'Ticket4')], default='T1', max_length=100),
        ),
    ]