# Generated by Django 2.2.2 on 2019-07-22 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_quer1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quer1',
            name='use2',
        ),
        migrations.AlterModelTable(
            name='quer1',
            table='quer1',
        ),
    ]