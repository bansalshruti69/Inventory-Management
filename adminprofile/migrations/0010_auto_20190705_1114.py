# Generated by Django 2.2.2 on 2019-07-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminprofile', '0009_auto_20190705_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Location',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
