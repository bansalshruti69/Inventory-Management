# Generated by Django 2.2.2 on 2019-06-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20190628_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Employee_Id',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
