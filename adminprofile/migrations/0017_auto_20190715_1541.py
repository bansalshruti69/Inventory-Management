# Generated by Django 2.2.2 on 2019-07-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminprofile', '0016_auto_20190710_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Date_Of_Order',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='Delivered_Date',
            field=models.DateField(null=True),
        ),
    ]
