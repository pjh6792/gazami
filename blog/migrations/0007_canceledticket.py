# Generated by Django 2.2.3 on 2019-08-15 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20190816_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanceledTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_bank', models.CharField(default='', max_length=200)),
                ('refund_account', models.BigIntegerField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Ticket')),
            ],
        ),
    ]
