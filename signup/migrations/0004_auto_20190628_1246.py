# Generated by Django 2.2.2 on 2019-06-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20190628_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Employee_Id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
